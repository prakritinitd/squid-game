const button = document.querySelector( ".about" );
const homeSection = document.querySelector( ".section-home" );
const aboutSection = document.querySelector( ".section-about" );
const homeButton = document.querySelector( ".home-button" );
const aboutButton = document.querySelector( ".about-button" );

Splitting();
const character = document.querySelectorAll(
    ".content__paragraph .word > .char"
);

const aboutTimeline = gsap.timeline( {
    paused: true,
} );
aboutTimeline.set( ".content__figure-caption", {
    opacity: 0,
} );
aboutTimeline.set( character, {
    y: "100%",
} );
aboutTimeline
    .set( ".content__figure-img", {
        y: "100%",
        rotation: -4,
        opacity: 0,
    } )
    .to( " h1 ", { opacity: 0, yPercent: 115 } )
    .to( " h2 ", { opacity: 0, y: "150%" } )
    .to( " h3  ", { opacity: 0, y: "125%" } )
    .to( " h4 ", {
        opacity: 0,
        x: "-10000",
    } )

    .to( ".distortion", {
        opacity: 0,
        y: "20",
    } )
    .add( () => {
        homeSection.classList.toggle( "visible" );
        aboutSection.classList.toggle( "visible" );
    } )
    .to( character, {
        opacity: 1,
        y: "0%",
        stagger: 0.08,
        duration: 0.3,
    } )
    .to( ".content__figure-img", {
        opacity: 1,
        y: "0%",
        rotation: 0,
        duration: 0.3,
    } )
    .to( ".content__figure-caption", {
        opacity: 1,
        duration: 0.3,
        ease: "expo.inOut",
    } );

var introAnim = gsap.timeline( {
    defaults: { duration: 1.5, ease: "expo.inOut" },
} );
introAnim
    .to( ".first", { top: "-100%" } )
    .to( ".second", { top: "-100%" }, 0.4 )
    .to( ".third", { top: "-100%" }, 0.5 )
    .addLabel( "introPanels" )
    .from(
        ".navbar  > *",
        {
            opacity: 0,
            y: "20",
            stagger: 0.08,
        },
        "introPanels"
    )
    .from(
        ".media ul li",
        {
            opacity: 0,
            x: "-20",
            stagger: 0.1,
        },
        "introPanels"
    )
    .from( " h1 ", { opacity: 0, yPercent: 115 }, "introPanels-=0.5" )
    .from( " h2 ", { opacity: 0, y: "150%" }, "introPanels-=0.7" )
    .from( " h3  ", { opacity: 0, y: "125%" }, "introPanels-=0.8" )
    .from(
        " h4 ",
        {
            opacity: 0,
            x: "-10000",
        },
        "introPanels"
    )

    .from(
        ".distortion",
        {
            opacity: 0,
            y: "20",
        },
        "introPanels+=0.5"
    );

homeButton.addEventListener( "click", ( e ) => {
    homeButton.classList.toggle( "active" );
    aboutButton.classList.toggle( "active" );
    aboutTimeline.play();
} );
aboutButton.addEventListener( "click", ( e ) => {
    homeButton.classList.toggle( "active" );
    aboutButton.classList.toggle( "active" );
    aboutTimeline.reverse();
} );


var countDownDate = new Date( "Jan 15, 2022 15:37:25" ).getTime();

// Update the count down every 1 second
var x = setInterval( function () {

    // Get today's date and time
    var now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor( distance / ( 1000 * 60 * 60 * 24 ) );
    var hours = Math.floor( ( distance % ( 1000 * 60 * 60 * 24 ) ) / ( 1000 * 60 * 60 ) );
    var minutes = Math.floor( ( distance % ( 1000 * 60 * 60 ) ) / ( 1000 * 60 ) );
    var seconds = Math.floor( ( distance % ( 1000 * 60 ) ) / 1000 );

    // Display the result in the element with id="demo"
    document.getElementById( "demo" ).innerHTML = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

    // If the count down is finished, write some text
    if ( distance < 0 ) {
        clearInterval( x );
        document.getElementById( "demo" ).innerHTML = "EXPIRED";
    }
}, 1000 );