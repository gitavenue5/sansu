function income(ttt){
    $(document).ready(function(){
        $.getJSON('/api/wrbank_api', function(data){

            if(data.length>0){
                //$('#wbl').empty();
            
                $.each(data, function(){
                    var t = '<li>'+ this['wrbank_date'] + '</li><li>' 
                        + this['wrbank_deposit_withdrawal'] + '</li><li>' + comma(this['wrbank_money1']) + '</li><li style="width:200px;">' + this['wrbank_note']
                            + '</li><li>' + comma(this['wrbank_money2']) + '</li><li>' + comma(this['wrbank_money3']) + '</li><li>' 
                                + comma(this['wrbank_aggregate']) + '</li><li>' + comma(this['wrbank_loan_balance']) + '</li><li>' + comma(this['wrbank_bankbook_balance']) + '</li>' ; 
                          
             
                    if(this['wrbank_deposit_withdrawal']==ttt){
                        $('#wbl').append('<p><ul>' + t +'</ul></p>').css({'margin': '20px'});  
                        
                    };//if                       
                })//each
            }//if
        })//json
    })//ready
};//income


function head(item){
    header = '<tr>';
    for(key in item){
        header += '<th>' + key + '</th>';        
    }
    header += '</tr>'
    return header;
};