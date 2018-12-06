$(function() {

    // Managing dynamic API albumlist and songlist query
    let $titleField = $('#id_title');
    let $yearField = $('#id_release_year');
    let $songListField = $('#id_songlist');
    let $albumLinks = $('.visible');
    let $discogsId = $('#id_discogs_id');
    console.log($albumLinks);
    for (let $eachLink of $albumLinks) {
        $($eachLink).on('click', function () {
            console.log("ustawiono atrybut tytułu");
            $titleField.attr( "value", $.trim($(this).text()) );
            console.log("nowy tytuł:", $titleField.attr('value'));
            console.log("id albumu w discogs:", $(this).attr('id'));
            $discogsId.attr("value", $.trim($(this).attr('id')));
            console.log("data wydania albumu:", $(this).attr('data-year'));
            $yearField.attr( "value", $.trim($(this).attr('data-year')));
            console.log("nowa data:", $yearField.attr('value'));

            $.ajax({
                type: 'GET',
                url: `http://api.discogs.com/releases/${$(this).attr('id')}`,
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

                })
                .fail(function () {
                    console.log("No tracklist");
                    $songListField.attr('value', "No songs in database");
                })

        })
    }
 // Managing a clever browse album view
    let $browseContainer = $('#browseContainer');
    $('#id_browse_band').on('change', function () {
        let $queryBandId = $(this).children("option:selected").attr('value');
        console.log($queryBandId);
        $.ajax({
            type: 'GET',
            url: `/show-albums-by-artist/${$queryBandId}`,
        })
            .done(function (response) {
                console.log("Odpowiedź własnego serwera:", response);
                $('#browseContainer div').remove();
                if (response.length === 0) {
                    let $newDiv = `<div>Brak nagrań</div>`;
                    $browseContainer.append($newDiv);
                }
                else {
                     for (let $each_album of response) {
                    let $newDiv = `<div>${$each_album['title']}</div>`;
                    $browseContainer.append($newDiv);
                }
                }
        })
            .fail(function () {
                console.log("Connection error");
                $('#browseContainer div').remove();
                let $newDiv = `<div>Error 404</div>`;
                    $browseContainer.append($newDiv);
            })
    });

});