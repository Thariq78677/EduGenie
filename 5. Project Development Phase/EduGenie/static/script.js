const taskConfig = {
  qa: {
    label: 'Ask Question',
    placeholder: 'Ask your academic question here...',
    endpoint: '/qa',
    payloadKey: 'question',
    render: (data) => {
      return `
        <div class="card">
          <h3>Answer</h3>
          <div class="answer-text">${escapeHtml(data.answer || '')}</div>
        </div>
      `;
    },
  },
  explain: {
    label: 'Explain Topic',
    placeholder: 'Enter a topic like Photosynthesis or Machine Learning...',
    endpoint: '/explain',
    payloadKey: 'topic',
    render: (data) => {
      return `
        <div class="card">
          <h3>Explanation</h3>
          <div class="explanation-text">${escapeHtml(data.explanation || '')}</div>
        </div>
      `;
    },
  },
  quiz: {
    label: 'Generate Quiz',
    placeholder: 'Enter a topic or passage to generate a 3-question quiz...',
    endpoint: '/quiz',
    payloadKey: 'text',
    render: (data) => {
      const quiz = Array.isArray(data.quiz) ? data.quiz : [];
      window.__lastQuizData = quiz;
      const questionCards = quiz.map((item, index) => {
        const options = item.options.map((option) => {
          return `
            <label class="option-row">
              <input type="radio" name="q-${index}" value="${escapeAttribute(option)}" />
              <span>${escapeHtml(option)}</span>
            </label>
          `;
        }).join('');

        return `
          <div class="quiz-card" data-question-index="${index}">
            <h4>Question ${index + 1}</h4>
            <p>${escapeHtml(item.question || '')}</p>
            <div class="quiz-options">${options}</div>
          </div>
        `;
      }).join('');

      return `
        <div class="card">
          <h3>Quiz</h3>
          <div class="quiz-list">${questionCards}</div>
          <button id="submitQuizBtn" class="primary-btn">Submit Quiz</button>
        </div>
      `;
    },
  },
  summarize: {
    label: 'Summarize Text',
    placeholder: 'Paste a long educational passage here...',
    endpoint: '/summarize',
    payloadKey: 'text',
    render: (data) => {
      return `
        <div class="card">
          <h3>Summary</h3>
          <div class="summary-text">${escapeHtml(data.summary || '')}</div>
        </div>
      `;
    },
  },
  learn: {
    label: 'Learning Path',
    placeholder: 'Enter a topic such as SQL, Python, or Cloud Computing...',
    endpoint: '/learn/recommendations',
    payloadKey: 'topic',
    render: (data) => {
      const recommendations = data.recommendations || {};
      const order = Array.isArray(recommendations.suggested_learning_order) ? recommendations.suggested_learning_order : [];
      const resources = Array.isArray(recommendations.resource_types) ? recommendations.resource_types : [];
      const practice = Array.isArray(recommendations.practice_suggestions) ? recommendations.practice_suggestions : [];

      return `
        <div class="card">
          <h3>Learning Recommendations</h3>
          <div class="learning-block">
            <p><strong>Beginner:</strong> ${escapeHtml(recommendations.beginner_level || '')}</p>
            <p><strong>Intermediate:</strong> ${escapeHtml(recommendations.intermediate_level || '')}</p>
            <p><strong>Advanced:</strong> ${escapeHtml(recommendations.advanced_level || '')}</p>
            <p><strong>Suggested Order:</strong> ${escapeHtml(order.join(' → ') || '')}</p>
            <p><strong>Practice:</strong> ${escapeHtml(practice.join(' • ') || '')}</p>
            <p><strong>Resource Types:</strong> ${escapeHtml(resources.join(', ') || '')}</p>
            <p><strong>Timeline:</strong> ${escapeHtml(recommendations.timeline || '')}</p>
          </div>
        </div>
      `;
    },
  },
};

const taskGrid = document.getElementById('taskGrid');
const userInput = document.getElementById('userInput');
const submitBtn = document.getElementById('submitBtn');
const loading = document.getElementById('loading');
const errorBox = document.getElementById('errorBox');
const resultArea = document.getElementById('resultArea');

let activeTask = 'qa';

function escapeHtml(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function escapeAttribute(value) {
  return escapeHtml(value).replace(/`/g, '&#96;');
}

function setActiveTask(task) {
  activeTask = task;
  const cards = document.querySelectorAll('.task-card');
  cards.forEach((card) => {
    card.classList.toggle('active', card.dataset.task === task);
  });

  const config = taskConfig[task];
  userInput.placeholder = config.placeholder;
  userInput.value = '';
  resultArea.innerHTML = '';
  hideError();
}

function showLoading(show) {
  loading.classList.toggle('hidden', !show);
  submitBtn.disabled = show;
  submitBtn.style.opacity = show ? '0.7' : '1';
}

function showError(message) {
  errorBox.textContent = message;
  errorBox.classList.remove('hidden');
}

function hideError() {
  errorBox.textContent = '';
  errorBox.classList.add('hidden');
}

function renderResult(content) {
  resultArea.innerHTML = content;

  const submitQuizBtn = document.getElementById('submitQuizBtn');
  if (submitQuizBtn) {
    submitQuizBtn.addEventListener('click', handleQuizSubmission);
  }
}

async function callApi(endpoint, payload) {
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const message = data.detail || 'Something went wrong while contacting the server.';
    throw new Error(message);
  }

  return data;
}

async function handleSubmit() {
  const text = userInput.value.trim();
  if (!text) {
    showError(`Please enter a ${taskConfig[activeTask].label.toLowerCase()}.`);
    return;
  }

  const config = taskConfig[activeTask];
  const payload = { [config.payloadKey]: text };

  showLoading(true);
  hideError();

  try {
    const result = await callApi(config.endpoint, payload);
    renderResult(config.render(result));
  } catch (error) {
    showError(error.message || 'Unable to process your request.');
  } finally {
    showLoading(false);
  }
}

function handleQuizSubmission() {
  const quizCards = document.querySelectorAll('.quiz-card');
  const quizList = document.querySelector('.quiz-list');
  if (!quizList) return;

  const priorResults = quizList.querySelectorAll('.quiz-result');
  priorResults.forEach((node) => node.remove());

  let score = 0;

  quizCards.forEach((card) => {
    const questionIndex = Number(card.dataset.questionIndex);
    const answerKey = `q-${questionIndex}`;
    const chosenValue = card.querySelector(`input[name="${answerKey}"]:checked`);
    const selectedText = chosenValue ? chosenValue.value : null;
    const questionData = window.__lastQuizData?.[questionIndex];

    const outcome = document.createElement('div');
    outcome.className = 'quiz-result';

    if (questionData) {
      if (selectedText === questionData.correct_answer) {
        score += 1;
        outcome.innerHTML = `<div class="correct">✓ Correct</div><p>Correct answer: ${escapeHtml(questionData.correct_answer)}</p><p>${escapeHtml(questionData.explanation)}</p>`;
      } else {
        outcome.innerHTML = `<div class="wrong">✗ Incorrect</div><p>Your answer: ${escapeHtml(selectedText || 'No answer selected')}</p><p>Correct answer: ${escapeHtml(questionData.correct_answer)}</p><p>${escapeHtml(questionData.explanation)}</p>`;
      }
    } else {
      outcome.innerHTML = '<div class="wrong">✗ Quiz data unavailable</div>';
    }

    quizList.appendChild(outcome);
  });

  const scoreCard = document.createElement('div');
  scoreCard.className = 'quiz-result';
  scoreCard.innerHTML = `<div class="score-badge">Score: ${score} / ${quizCards.length}</div>`;
  quizList.appendChild(scoreCard);
}

taskGrid.addEventListener('click', (event) => {
  const card = event.target.closest('.task-card');
  if (!card) return;
  setActiveTask(card.dataset.task);
});

submitBtn.addEventListener('click', handleSubmit);

userInput.addEventListener('keydown', (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
    handleSubmit();
  }
});

setActiveTask(activeTask);
