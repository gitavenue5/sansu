function com(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };

// 글 내용 감추기
function wrhidden(){
    $(document).ready(function(){
      $('#kk').click(function(){
        $('#wb').css({'display': 'none'});
      });//ctdck
    });//ready function end
};//hidden function end

$(function(){
    $('#kk').click(function(){
      $('#wb').css({'display': 'none'});
    });
  });

// income(this.value) 셀렉터 함수
$(function(){
    $('#wbls').on('change', function(){
      income(this.value);
    });//on
  });//function



function income(ttt){
    $(document).ready(function(){
        $.getJSON('/api/wrbank_api', function(data){

            if(data.length>0){
                $('#wb').empty();

                $.each(data, function(){

                     t = '<tbody><tr><td>'+ this['wrbank_date'] + '</td><td>'
                        + this['wrbank_deposit_withdrawal'] + '</td><td>' + com(this['wrbank_money1']) + '</td><td style="width:200px;">' + this['wrbank_note']
                            + '</td><td>' + com(this['wrbank_money2']) + '</td><td>' + com(this['wrbank_money3']) + '</td><td>'
                                + com(this['wrbank_aggregate']) + '</td><td>' +
                                com(this['wrbank_loan_balance']) + '</td><td>' +
                                com(this['wrbank_bankbook_balance']) + '</td></tr></tbody>';

                   //var u = '<thead><tr><th>날 자</th><th>입출금</th><th>금 액</th><th>비 고</th><th>대출이자</th><th>대출원금</th><th>이자+원금</th><th>대출잔액</th><th>통장잔액</th></tr></thead>';

                   if(this['wrbank_deposit_withdrawal']==ttt){

                        $("table").append(t).css({'margin-top': '20px','margin-bottom': '20px'});

                    };//if
                });//each
            };//if
        });//json
    });//ready
};//income
