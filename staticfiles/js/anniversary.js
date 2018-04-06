 
    $(document).ready(function(){ 
        $.getJSON('/api/anniversary_api', function(data){
            if(data.length>0){
                   
               // $('#birthday').empty();  
                var now = new Date();
                var year = now.getFullYear();
                var month = (now.getMonth() + 1) ;
                var day = now.getDate();  

                if((month+"").length<2){
                    month = "0" + month;
                }// if getMonth
                
                if((day + "").length < 2){
                    day = "0" + day;
                }// if getday


                var today = year + '-' + month + '-' + day;
                    console.log(today)
                $.each(data, function(){
                    var b = this['anniversary_date'];           
                                            
                        if(b==today){
                            $('#birthday').show().append('<span style="font-weight: bold; font-family:바탕;">' + this['anniversary_name']  + '</span>' + "" + '님의 생일을 축하합니다!') ;
                            
                        }//if
                        
                    
                });// each
            };//if
        });//getjson
    });// ready

    