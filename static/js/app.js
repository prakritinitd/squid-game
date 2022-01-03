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