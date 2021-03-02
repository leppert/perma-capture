// from https://docs.djangoproject.com/en/2.2/ref/csrf/#ajax
export function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export function snakeToPascal(str='') {
    return str.split('_').map(word => word.slice(0,1).toUpperCase() + word.slice(1)).join('');
}
