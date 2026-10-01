// ===== ТЕСТ: ВИБІР ВАРІАНТА =====
function checkChoice(btn, isCorrect) {
    const parent = btn.closest('.options');
    parent.querySelectorAll('.option').forEach(b => {
        b.disabled = true;
        if (b.dataset.correct === 'true') b.classList.add('correct');
    });
    if (!isCorrect) btn.classList.add('incorrect');

    const feedback = parent.parentElement.querySelector('.feedback');
    if (feedback) {
        feedback.textContent = isCorrect ? '✅ Правильно!' : '❌ Неправильно. Дивіться правильну відповідь вище.';
        feedback.className = 'feedback ' + (isCorrect ? 'correct' : 'incorrect');
    }
}

// ===== ТЕСТ: ВВЕДЕННЯ ВІДПОВІДІ =====
function checkInput(btn, correctAnswer, tolerance = 0.001) {
    const wrap = btn.closest('.input-answer');
    const input = wrap.querySelector('input');
    const feedback = wrap.parentElement.querySelector('.feedback');

    // Нормалізуємо обидва значення: кома → крапка, прибираємо пробіли
    const normalize = (s) => String(s).trim().replace(/\s/g, '').replace(',', '.');
    const userAnswer = normalize(input.value);
    const correctNormalized = normalize(correctAnswer);

    if (!userAnswer) {
        feedback.textContent = '⚠️ Введіть відповідь';
        feedback.className = 'feedback incorrect';
        return;
    }

    let isCorrect;
    const userNum = parseFloat(userAnswer);
    const correctNum = parseFloat(correctNormalized);

    if (!isNaN(userNum) && !isNaN(correctNum)) {
        // Числове порівняння з допуском
        isCorrect = Math.abs(userNum - correctNum) <= tolerance;
    } else {
        // Текстове порівняння (без урахування регістру)
        isCorrect = userAnswer.toLowerCase() === correctNormalized.toLowerCase();
    }

    input.classList.remove('correct', 'incorrect');
    input.classList.add(isCorrect ? 'correct' : 'incorrect');
    input.disabled = true;
    btn.disabled = true;

    feedback.textContent = isCorrect
        ? '✅ Правильно!'
        : `❌ Неправильно. Правильна відповідь: ${correctAnswer}`;
    feedback.className = 'feedback ' + (isCorrect ? 'correct' : 'incorrect');
}
// Enter у полі введення = клік по кнопці
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.matches('.input-answer input')) {
        const btn = e.target.closest('.input-answer').querySelector('.btn');
        if (!btn.disabled) btn.click();
    }
});

// ===== ПОКАЗ РОЗВ'ЯЗКУ =====
function toggleSolution(btn) {
    const question = btn.closest('.question');
    const solution = question.querySelector('.solution');
    solution.classList.toggle('show');
    btn.textContent = solution.classList.contains('show') ? '🙈 Сховати розв\'язок' : '👁 Показати розв\'язок';
}