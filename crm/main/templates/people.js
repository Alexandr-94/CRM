const domain = 'http://127.0.0.1:8000/';

function listLoader() {
    $.getJSON(domain + 'api/people/', function(data)
    {
        let s = '<ul>', d;
        for (let i = 0; i < data.length; i++)
        {
            d = data[i];
            s += '<li id="' + d.id + '">' + d.last_name + ' ' + d.first_name + ' ' + d.patronymic + '<div>' + d.skills + '</div></li>';
        }
        s += '</ul>';

        $('#list_0').html(s);
    });
}
listLoader();