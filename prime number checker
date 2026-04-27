<!DOCTYPE html>
<html>
<head>
    <title>Prime Checker</title>
</head>
<body>

<h2>Check Prime Number</h2>

<input type="number" id="num" placeholder="Enter number">
<button onclick="checkPrime()">Check</button>

<p id="result"></p>

<script>
function checkPrime() {
    let num = parseInt(document.getElementById("num").value);
    let isPrime = true;

    if (num <= 1) isPrime = false;

    for (let i = 2; i <= num / 2; i++) {
        if (num % i === 0) {
            isPrime = false;
            break;
        }
    }

    document.getElementById("result").innerText =
        isPrime ? num + " is Prime" : num + " is NOT Prime";
}
</script>

</body>
</html>