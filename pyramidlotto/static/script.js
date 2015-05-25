/**
 * Created by PaulFranken on 17/05/15.
 */
console.log("pst");

$(document).ready(function(){
    $("#getTickets").on('click', function(){
        console.log("hoi");
        $("#ticketsDiv").css("opacity", 1);
    })
    $("#playButton").on('click', function(){
        console.log("players");
        $("#playersDiv").css("opacity", 1);
        getPlayers();
    })
    $("#playBtn").on('click', function(){
        play();
    })
});

function getTickets(){
    var name = $("#ticketsText").val()
    var amount = $("#ticketsNumber").val()

    jQuery.ajax({
        url : 'tickets_view',
        type : 'POST',
        data : {amount: amount, name : name},
        dataType : 'json',
        success : function(data){
            $("#ticketList").append('Your tickets are:');
            $("#ticketList").append('<br>');

            $.each(data.ticket, function(i, item){
                $("#ticketList").append(item.toString());
                $("#ticketList").append('<br>');
            })
        }
    });
}

function getPlayers(){
    jQuery.ajax({
        url : 'players_view',
        type : 'POST',
        dataType : 'json',
        success : function(data){
            console.log(data.names[0][0])
            $.each(data.names, function(i, item){
                $("#players").append('<option>' + item + '</option>');
            })
        }
    })
}

function play(){
    var playerName = $("#players option:selected").text();
    console.log(playerName);
    jQuery.ajax({
        url : 'play_view',
        type : 'POST',
        dataType : 'json',
        data : {name: playerName},
        success: function(data){
            console.log(data.tickets);
            console.log(data.winningNumber);
            $("#results").append("The winning number is: ");
            $("#results").append('<br>');
            $("#results").append(data.winningNumber.toString());
            $("#results").append('<br><br>');

            var prize = 0;
            var grandPrizes = 0;

            $.each(data.tickets, function(x, item){
                var points = 0;
                var answer = " without a matching powerball.";
                var powerball = false;

                var summary;

                $.each(item, function(y, subItem){
                    $.each(data.winningNumber, function(z, wSub){
                        if(z <= 4){
                            if(subItem == wSub){
                            points++;
                            }
                        }
                    })
                })

                if(item[5] == data.winningNumber[5]){
                    answer = " with a matching powerball";
                    powerball = true;
                }
                if(powerball){
                    if(points == 5){
                        grandPrizes++;
                    }
                    else{
                        prize = prize + calculatePrize(points, powerball);
                    }
                }
                else{
                    prize = prize + calculatePrize(points, powerball)
                }

                $("#results").append("<p class='result'>");
                $("#results").append(item.toString());
                $("#results").append("  " + points + " numbers match" + answer + "</p>");
            })
            $("#results").append("<br>");
            $("#results").append("You have won " + prize + "$ in prizes and won " + grandPrizes + " grand prizes!");
            $("#results").append("You have spent " + (data.tickets.length * 2) + "$ in tickets")

            $("#results").css("opacity", 1);
        }
    })
}

function calculatePrize(points, power){
    if(points == 1 || points == 0){
        if(power){
            return 4;
        }
        else{
            return 0;
        }

    }
    else if(points == 2){
        if(power){
            return 7;
        }
        else{
            return 0;
        }
    }
    else if(points == 3){
        if(power){
            return 100
        }
        else{
            return 7;
        }
    }
    else if(points == 4){
        if(power){
            return 10000;
        }
        else{
            return 100
        }
    }
    else if(points == 5){
        if(power){
            return -1;
        }
        else{
            return 1000000;
        }
    }
}