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
function checkInput(btn, correctAnswer, tolerance = 0) {
    const wrap = btn.closest('.input-answer');
    const input = wrap.querySelector('input');
    const feedback = wrap.parentElement.querySelector('.feedback');
    const userAnswer = input.value.trim().replace(',', '.');

    if (!userAnswer) {
        feedback.textContent = '⚠️ Введіть відповідь';
        feedback.className = 'feedback incorrect';
        return;
    }

    let isCorrect;
    const userNum = parseFloat(userAnswer);
    const correctNum = parseFloat(correctAnswer);

    if (!isNaN(userNum) && !isNaN(correctNum)) {
        isCorrect = Math.abs(userNum - correctNum) <= tolerance;
    } else {
        isCorrect = userAnswer.toLowerCase() === correctAnswer.toLowerCase();
    }

    input.classList.remove('correct', 'incorrect');
    input.classList.add(isCorrect ? 'correct' : 'incorrect');
    input.disabled = true;
    btn.disabled = true;

    feedback.textContent = isCorrect ? '✅ Правильно!' : `❌ Неправильно. Правильна відповідь: ${correctAnswer}`;
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