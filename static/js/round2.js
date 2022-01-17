const TIME   = document.getElementById('timeLeft').innerText
const THEURL = window.location.origin
var INPUT  = document.getElementById('input')
var SUBMIT = document.getElementById('submit')
var tyme = 1;

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
        if (tyme === 1){
            tyme += 1
            document.getElementById('input').remove()
            document.getElementById('submit').remove()

            axios.get(`${THEURL}/pandorabox`).then(res =>{
                console.log(res.data.message);
            }).catch(err => {
                console.error(err);
            })
        }
            return
    }

    document.getElementById("timer")
        .innerHTML =
        '<div>' + m + '<span>minutes</span></div>' +
        '<div>' + s + '<span>seconds</span></div>';
    return;
}
setInterval('updateTimer()', 1000); // 1000 ms latency, every 1000ms there will be rerendering