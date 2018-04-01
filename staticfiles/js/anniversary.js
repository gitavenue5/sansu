$(document).ready(function(){
    $.getJSON('/api/anniversary_api', function(data){
        if( data.length > 0){
            $('#uuu').empty();            
            $.each(data, function(){
                
                var kk = '<ul><li>' + this['anniversary_date'] + '<li></li>' + this['anniversary_name'] + '</li></ul>';
                
                     //$('#uuu').append(kk);
          
                
            })//each
        }// if
    });// getJson
})// ready
