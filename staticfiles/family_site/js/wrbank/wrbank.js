function income(ttt){
    $(document).ready(function(){
        $.getJSON('/api/wrbank_api', function(data){

            if(data.length>0){
                $('#wbl').empty();
            
                $.each(data, function(){
                    var t = '<td style="width:10%";>'+ this['wrbank_date'] + '</td><td style="width:6%";>' 
                        + this['wrbank_deposit_withdrawal'] + '</td><td style="width:10%";>' + comma(this['wrbank_money1']) + '</td><td style="width:16%";>' + this['wrbank_note']
                            + '</td><td style="width:10%";>' + comma(this['wrbank_money2']) + '</td><td style="width:10%";>' + comma(this['wrbank_money3']) + '</td><td>' 
                                + comma(this['wrbank_aggregate']) + '</td><td style="width:8%";>' + comma(this['wrbank_loan_balance']) + '</td><td style="width:10%";>' + comma(this['wrbank_bankbook_balance']) + '</td>' ; 
                                                            
                    if(this['wrbank_deposit_withdrawal']==ttt){
                        $('#wbl').append('<table class="table table-bordered table-hover"><tr>'+ t + '</tr></table>').css({'margin': '20px'})};

                       
                })//each
            }//if
        })//json
    })//ready
};//income