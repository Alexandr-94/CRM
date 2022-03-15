const domain = 'http://127.0.0.1:8000/';

function listLoader() {
    $.getJSON(domain + 'api/company/', function(data)
    {
        let s = '<ul>', d;
        for (let i = 0; i < data.length; i++)
        {
            d = data[i];
            s += '<li id="' + d.id + '">' + d.name + '<div>' + d.description + '</div></li>';
        }
        s += '</ul>';

        $('#list_1').html(s);
    });
}
listLoader();