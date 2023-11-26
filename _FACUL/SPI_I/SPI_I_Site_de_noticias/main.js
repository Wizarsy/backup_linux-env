const html = document.querySelector("html")
const checkbox = document.querySelector("input[name=theme]")

const getStyle = (element, style) =>
  window
    .getComputedStyle(element)
    .getPropertyValue(style)


const initialColors = {
  bg: getStyle(html, "--bg"),
  bgPanel: getStyle(html, "--bg-panel"),
  colorHeadings: getStyle(html, "--color-headings"),
  colorText: getStyle(html, "--color-text"),
}

const darkMode = {
  bg: "#333333",
  bgPanel: "#434343",
  colorHeadings: "#FCFCFC",
  colorText: "#B5B5B5"
}

const transformKey = key =>
  "--" + key.replace(/([A-Z])/, "-$1").toLowerCase()


const changeColors = (colors) => {
  Object.keys(colors).map(key =>
    html.style.setProperty(transformKey(key), colors[key])
  )
}


checkbox.addEventListener("change", ({ target }) => {
  target.checked ? changeColors(darkMode) : changeColors(initialColors)
})

//////////////////////////////////////////////////////////////////////////

window.onload = function Destaque(){
  fetch('lib/data.json')
  .then(function(response){
      return response.json();
  })
  .then(function(images){
      let html = '';
      images.forEach(function(image){
          html += `
              <li>
              <a target="_blank" href="${image.news_url}">
                <img src="${image.news_image}">
              </a>

              <a target="_blank" href="${image.news_url}">
                ${image.news}
              </a>
              </li>
          `;
      });
      document.getElementById("noticias").innerHTML = html;
  });

}

//////////////////////////////////////////////////////////////////////////

const videos = [{
  title: "How Dune's Sandworms Swim | Because Science",
  url: "https://www.youtube.com/watch?v=5-iu7j9z5Vo"
},
{
  title: "How Much Would a DEATH STAR Cost? | Because Science",
  url: "https://www.youtube.com/watch?v=hrImnLihTV8"
},
{
  title: "What Dinosaurs ACTUALLY Looked Like? | Kurzgesagt – In a Nutshell",
  url: "https://www.youtube.com/watch?v=xaQJbozY_Is"

},
{
  title: "Live 01/02/2022 - Números do Brasil voltam a piorar e variante BA.2 | Atila Iamarino",
  url: "https://www.youtube.com/watch?v=iD_d9pWsuLY"
},
{
  title: "O Dia que os Dinossauros Morreram - Minuto por Minuto | Kurzgesagt – In a Nutshell",
  url: "https://www.youtube.com/watch?v=dFCbJmgeHmA"
},
{
  title: "Construir uma base em Marte é uma péssima ideia: Vamos construí-la! | Kurzgesagt – In a Nutshell",
  url: "https://www.youtube.com/watch?v=uqKGREZs6-w"
},
{
  title: "Why 3D Printing Batteries Matters | Undecided with Matt Ferrell",
  url: "https://www.youtube.com/watch?v=Jlt8_z86F-o"
},
{
  title: "FIM DA MONTAGEM DO JAMES WEBB! O ESPELHO PRIMÁRIO! | Space Today",
  url: "https://www.youtube.com/watch?v=60ljQv-EvQo"
},
{
  title: "Why Wind Power Ships May Be The Future of Transportation | Undecided with Matt Ferrell",
  url: "https://www.youtube.com/watch?v=MdI191-vNlc"
},
{
  title: "ORIGEM DOS DINOSSAUROS (TRIÁSSICO) | Canal do Pirula",
  url: "https://www.youtube.com/watch?v=q4SmMz-qUxc"
}
];

const title = document.getElementById("title")
const list = document.getElementById("videos")

title.addEventListener("keyup", function () {

  const matchs = videos.filter(value => {

    return value.title.indexOf(this.value) !== -1;

  });

  list.innerHTML = "";
  for (let videos of matchs) {
    list.innerHTML += "<li><a href='" + videos.url + "'>" + videos.title + "</a></li>"
  }
})