// let data

// const getData = async () => {
//     const response = await fetch('http://127.0.0.1:5000/');
//     data = await response.json();
// }

// getData();
// console.log({ data });

function get_data_from_url(url){
    var http_req = new XMLHttpRequest();
    http_req.open("GET",url,false);
    http_req.send(null);
    return http_req.responseText;          
}

let apiUrl = 'http://127.0.0.1:5000/';
let data = JSON.parse(get_data_from_url(apiUrl));

// const body = document.querySelector('body');
// const link = document.getElementById('link');
// link.setAttribute("href", data.url);
// const image = document.getElementById('cover');
// image.setAttribute("src", data.info.cover);
// const title = document.getElementById('title');
// const artistTitle = document.getElementById('artist-title');
// const tagsTitle = document.getElementById('tags-title');

// document.getElementById('link').innerHTML=`<a href=${data.url} id='link'></a>`;
// document.getElementById('cover').innerHTML=`<img src=${data.info.cover} alt="cover" id="cover">`;

window.onload = function main() {
    const body = document.getElementsByTagName("BODY")[0];

    const a = document.getElementById('link');
    a.setAttribute("href", data.url);
    a.setAttribute("id", "link");

    const img = document.getElementById('cover');
    img.setAttribute("src", data.info.cover);
    img.setAttribute("id", "cover");

    const title = document.getElementById('title');
    title.innerHTML=data.info.title;

    const artistTitle = document.getElementById('artist-title');
    artistTitle.innerHTML="Artists";

    const artistsArray = data.info.artists;
    artistsArray.forEach(a => {
        const artists = document.createElement('p');
        artists.innerHTML=a;
        artists.setAttribute("class", "artists");
        artistTitle.append(artists);
    })
    

    const tagsTitle = document.getElementById('tags-title');

    const tagsArray = data.info.tags;
    tagsArray.forEach(t => {
        const tags = document.createElement('p');
        tags.innerHTML=t;
        tags.setAttribute("class", "tags");
        tagsTitle.append(tags);
    })


    // body.append(a);
    // a.append(img);
}


