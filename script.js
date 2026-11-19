
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const box = 20;

let snake = [{ x: 200, y: 200 }];
let food = {
    x: 100,
    y: 100
};

let direction = "RIGHT";
let score = 0;
let gameOver = false;

document.addEventListener("keydown", changeDirection);

function changeDirection(event) {
    if (event.key === "ArrowUp" && direction !== "DOWN")
        direction = "UP";
    else if (event.key === "ArrowDown" && direction !== "UP")
        direction = "DOWN";
    else if (event.key === "ArrowLeft" && direction !== "RIGHT")
        direction = "LEFT";
    else if (event.key === "ArrowRight" && direction !== "LEFT")
        direction = "RIGHT";
}

function drawGame() {
    if (gameOver) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    snake.forEach((part, index) => {
        ctx.fillStyle = index === 0 ? "#2ecc71" : "#27ae60";
        ctx.fillRect(part.x, part.y, box, box);
    });

    ctx.fillStyle = "red";
    ctx.fillRect(food.x, food.y, box, box);

    let head = { ...snake[0] };

    if (direction === "UP") head.y -= box;
    if (direction === "DOWN") head.y += box;
    if (direction === "LEFT") head.x -= box;
    if (direction === "RIGHT") head.x += box;

    if (
        head.x < 0 || head.x >= canvas.width ||
        head.y < 0 || head.y >= canvas.height ||
        snake.some(part => part.x === head.x && part.y === head.y)
    ) {
        gameOver = true;
        alert("Game Over! Your score: " + score);
        return;
    }

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        score++;
        document.getElementById("score").textContent = score;
        createFood();
    } else {
        snake.pop();
    }
}

function createFood() {
    food = {
        x: Math.floor(Math.random() * 20) * box,
        y: Math.floor(Math.random() * 20) * box
    };

    if (snake.some(part => part.x === food.x && part.y === food.y)) {
        createFood();
    }
}

function restartGame() {
    snake = [{ x: 200, y: 200 }];
    direction = "RIGHT";
    score = 0;
    gameOver = false;

    document.getElementById("score").textContent = score;
    createFood();
    clearInterval(game);
    game = setInterval(drawGame, 120);
}

let game = setInterval(drawGame, 120);
