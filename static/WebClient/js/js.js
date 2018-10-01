$(function(){
    $('#username').bind('input propertychange', function() {  
        $('#result').html($(this).val());  
    });  

}) 