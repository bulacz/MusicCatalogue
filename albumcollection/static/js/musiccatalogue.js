$(function() {
    var $titleField = $('#id_title');
    var $yearField = $('#id_release_year');
    var $albumLinks = $('.visible');
    console.log($albumLinks);
    for (var $eachLink of $albumLinks) {
        $($eachLink).on('click', function () {
            console.log("ustawiono atrybut tytułu");
            $titleField.attr( "value", $.trim($(this).text()) );
            console.log("nowy tytuł:", $titleField.attr('value'));
            console.log("id albumu w discogs:", $(this).attr('id'));
            console.log("data wydania albumu:", $(this).attr('data-year'));
            $yearField.attr( "value", $.trim($(this).attr('data-year')));
            console.log("nowa data:", $yearField.attr('value'));



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