const TIME = document.getElementById('timeLeft').innerText
const THEURL = window.location.origin
var SENTONCE = false
function updateTimer() {
    future = Date.parse(TIME);
    now = new Date();
    diff = future - now;

    days = Math.floor(diff / (1000 * 60 * 60 * 24));
    hours = Math.floor(diff / (1000 * 60 * 60));
    mins = Math.floor(diff / (1000 * 60));
    secs = Math.floor(diff / 1000);

    d = days;
    h = hours - days * 24;
    m = mins - hours * 60;
    s = secs - mins * 60;

    if (d < 0){
        document.getElementById("timer")
            .innerHTML = "<h3><strong>GAME OVER !</strong></h3>"
            return
    }

    document.getElementById("timer")
        .innerHTML =
        '<div>' + d + '<span>days</span></div>' +
        '<div>' + h + '<span>hours</span></div>' +        
        '<div>' + m + '<span>minutes</span></div>' +
        '<div>' + s + '<span>seconds</span></div>';
    return;
}
setInterval('updateTimer()', 100); // 100 ms latency, every 10ms there will be rerendering