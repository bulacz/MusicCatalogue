$(function() {
    let $titleField = $('#id_title');
    let $yearField = $('#id_release_year');
    let $songListField = $('#id_songlist');
    let $albumLinks = $('.visible');
    console.log($albumLinks);
    for (let $eachLink of $albumLinks) {
        $($eachLink).on('click', function () {
            console.log("ustawiono atrybut tytułu");
            $titleField.attr( "value", $.trim($(this).text()) );
            console.log("nowy tytuł:", $titleField.attr('value'));
            console.log("id albumu w discogs:", $(this).attr('id'));
            console.log("data wydania albumu:", $(this).attr('data-year'));
            $yearField.attr( "value", $.trim($(this).attr('data-year')));
            console.log("nowa data:", $yearField.attr('value'));
            $.ajax({
                type: 'GET',
                url: `http:////api.discogs.com/releases/${$(this).attr('id')}`,
                data: `?callback=callbackname`,
                })
                .done(function (res) {
                    let $songList = '';
                    console.log("Response:", res);
                    console.log("tracklista:", res['tracklist']);
                        for (let $eachSong of res['tracklist']) {
                            console.log("Tytuł:", $eachSong['title']);
                            $songList += `${$eachSong['title']} (${$eachSong['duration']}), `;
                        }
                        $songListField.attr('value', $songList);
                        console.log("Zawartośc listy piosenek w formie:", $songListField.attr('value'));
            });


    //          $form.on('submit', function (e) {
    //     e.preventDefault();
    //     $.ajax({
    //         url: apiUrl,
    //         data: {
    //             q: $('#search').val(),
    //         }
    //     })
    //         .done(function (res) {
    //             console.log(res);
    //             for (response of res.items) {
    //                 console.log(response.volumeInfo.title);
    //             }
    //         })
    //         .fail(function () {
    //             console.log();
    //         })
    //         .always(function () {
    //             console.log();
    //         })
    // });





        })
    }
//
//
//     success: function(data) {
//     $('#number').val("value = " + $('#number').val().replace("placeholder", data));
// }



//
// document.addEventListener('DOMContentLoaded', function () {
//     const $album_links = $('.visible');
//     for single_link of $album_links


//     $ApiContactor.on('click', function(event){
//     event.preventDefault("DSDSDSDSD");
// });

//
//         const $form = $('#searchForm');
//     const apiUrl = 'https://www.googleapis.com/books/v1/volumes';
//
//
//       $form.on('submit', function (e) {
//         e.preventDefault();
//         $.ajax({
//             url: apiUrl,
//             data: {
//                 q: $('#search').val(),
//             }
//         })
//             .done(function (res) {
//                 console.log(res);
//                 for (response of res.items) {
//                     console.log(response.volumeInfo.title);
//                 }
//             })
//             .fail(function () {
//                 console.log();
//             })
//             .always(function () {
//                 console.log();
//             })
//     });
// });

});