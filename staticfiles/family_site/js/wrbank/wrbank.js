function com(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };


$(function(){
    $('#wb_btn').click(function(){
      $('#wb').css({'display': 'none'});
    });
  });

// income(this.value) 셀렉터 함수
$(function(){
    $('#wbls').on('change',  function(){
      income(this.value);
    });//on
  });//function

function income(ttt){
    $(document).ready(function(){
        $.getJSON('/api/wrbank_api', function(data){
            var jjjj = '<tr><th>날 자</th><th>입출금</th><th>금 액</th><th>비 고</th><th>대출이자</th><th>대출원금</th><th>이자+원금</th><th>대출잔액</th><th>통장잔액</th></tr>'; 
            if(data.length>0){
                $('#wb').empty();
                $('#wb').prepend(jjjj); // <th></th> 삽입코드

                $.each(data, function(){

                     t = '<tbody><tr><td>'+ this['wrbank_date'] + '</td><td>'
                        + this['wrbank_deposit_withdrawal'] + '</td><td>' + com(this['wrbank_money1']) + '</td><td style="width:200px;">' + this['wrbank_note']
                            + '</td><td>' + com(this['wrbank_money2']) + '</td><td>' + com(this['wrbank_money3']) + '</td><td>'
                                + com(this['wrbank_aggregate']) + '</td><td>' +
                                com(this['wrbank_loan_balance']) + '</td><td>' +
                                com(this['wrbank_bankbook_balance']) + '</td></tr></tbody>';

                   //var u = '<thead><tr><th>날 자</th><th>입출금</th><th>금 액</th><th>비 고</th><th>대출이자</th><th>대출원금</th><th>이자+원금</th><th>대출잔액</th><th>통장잔액</th></tr></thead>';

                   if(this['wrbank_deposit_withdrawal']==ttt){

                        $("#wb").append(t).css({'margin-top': '20px','margin-bottom': '80px'});
                    };//if
                });//each
            };//if
        });//json
    });//ready
};//income

// 숨기기 버튼
$(function(){
    $('#kkk').on('click', function(){
      $('#k').hide();
    });
  });

// 우리은행 내역서 엑셀 파일 보기 숨기기.
$(function(){
    $("#woori_bank_show").click(function() {
            $('#woori_bank_pandas').toggle('fast');
             });
     });