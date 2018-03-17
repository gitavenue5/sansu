function income(ttt){
    $(document).ready(function(){
        $.getJSON('/api/wrbank_api', function(data){

            if(data.length>0){
<<<<<<< HEAD
                $('#wbl').empty();
            
                $.each(data, function(){
                    var t = '<td style="width:10%";>'+ this['wrbank_date'] + '</td><td style="width:6%";>' 
                        + this['wrbank_deposit_withdrawal'] + '</td><td style="width:10%";>' + comma(this['wrbank_money1']) + '</td><td style="width:16%";>' + this['wrbank_note']
                            + '</td><td style="width:10%";>' + comma(this['wrbank_money2']) + '</td><td style="width:10%";>' + comma(this['wrbank_money3']) + '</td><td>' 
                                + comma(this['wrbank_aggregate']) + '</td><td style="width:8%";>' + comma(this['wrbank_loan_balance']) + '</td><td style="width:10%";>' + comma(this['wrbank_bankbook_balance']) + '</td>' ; 
                                                            
                    if(this['wrbank_deposit_withdrawal']==ttt){
                        $('#wbl').append('<table class="table table-bordered table-hover"><tr>'+ t + '</tr></table>').css({'margin': '20px'})};

                       
=======
                //$('#wbl').empty();
            
                $.each(data, function(){
                    var t = '<li>'+ this['wrbank_date'] + '</li><li>' 
                        + this['wrbank_deposit_withdrawal'] + '</li><li>' + comma(this['wrbank_money1']) + '</li><li style="width:200px;">' + this['wrbank_note']
                            + '</li><li>' + comma(this['wrbank_money2']) + '</li><li>' + comma(this['wrbank_money3']) + '</li><li>' 
                                + comma(this['wrbank_aggregate']) + '</li><li>' + comma(this['wrbank_loan_balance']) + '</li><li>' + comma(this['wrbank_bankbook_balance']) + '</li>' ; 
                          
             
                    if(this['wrbank_deposit_withdrawal']==ttt){
                        $('#wbl').append('<p><ul>' + t +'</ul></p>').css({'margin': '20px'});  
                        
                    };//if                       
>>>>>>> 163298a352472d71eee27d553bee416aa8d313fe
                })//each
            }//if
        })//json
    })//ready
<<<<<<< HEAD
};//income
=======
};//income


function head(item){
    header = '<tr>';
    for(key in item){
        header += '<th>' + key + '</th>';        
    }
    header += '</tr>'
    return header;
};
>>>>>>> 163298a352472d71eee27d553bee416aa8d313fe
