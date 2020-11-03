function hidediv() {
    $('#alerts').removeClass('animate__animated animate__slideOutRight animate__fast').show().addClass('animate__animated animate__slideInRight animate__fast');

    $('#alerts').removeClass('animate__animated animate__slideInRight animate__fast').addClass('animate__animated animate__slideOutRight animate__fast');
}

setTimeout("hidediv()", 5000);