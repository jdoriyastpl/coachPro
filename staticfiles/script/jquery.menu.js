$(function () {
    var flag;
    if ($('body').hasClass('sidebar-colors')) {
        flag = true;
    } else {
        flag = false;
    }
    $('#menu-toggle').toggle(
        function () {
            if ($('#wrapper').hasClass('right-sidebar')) {
                $('body').addClass('right-side-collapsed')
                $('#sidebar .slimScrollDiv').css('overflow', 'initial');
                $('#sidebar .menu-scroll').css('overflow', 'initial');
            } else {
                $('body').addClass('left-side-collapsed').removeClass('sidebar-colors');
                $('#sidebar .slimScrollDiv').css('overflow', 'initial');
                $('#sidebar .menu-scroll').css('overflow', 'initial');
            }
        },
        function () {
            if ($('#wrapper').hasClass('right-sidebar')) {
                $('body').removeClass('right-side-collapsed');
                $('#sidebar .slimScrollDiv').css('overflow', 'hidden');
                $('#sidebar .menu-scroll').css('overflow', 'hidden');
            } else {
                $('body').removeClass('left-side-collapsed')
                if (flag == true) {
                    $('body').addClass('sidebar-colors');
                }
                $('#sidebar .slimScrollDiv').css('overflow', 'hidden');
                $('#sidebar .menu-scroll').css('overflow', 'hidden');
            }
        }
    );

    if ($('#wrapper').hasClass('right-sidebar')) {
        $('ul#side-menu li').hover(function () {
            if ($('body').hasClass('right-side-collapsed')) {
                $(this).addClass('nav-hover');
            }
        }, function () {
            if ($('body').hasClass('right-side-collapsed')) {
                $(this).removeClass('nav-hover');
            }
        });
    } else {
        $('ul#side-menu li').hover(function () {
            if ($('body').hasClass('left-side-collapsed')) {
                $(this).addClass('nav-hover');
            }
        }, function () {
            if ($('body').hasClass('left-side-collapsed')) {
                $(this).removeClass('nav-hover');
            }
        });
    }

});

//Chart js homepage data.
$(function () {
    var endpoint = '/api/courses/data/'
    var defaultData = []
    var labels = [];
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            course = data.course
            noStudent = data.no_students
            setChart()
        },
        error: function (error_data) {
            console.log("error")
            //                console.log(error_data)
        }
    })

    function setChart() {
        var ctx = document.getElementById("bar-chart");
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: course,
                datasets: [{
                    label: '# of Students',
                    data: noStudent,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 0.5
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                             display:true,
                          
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'No of Students'
                          }
                    }],
                    xAxes: [{
                        barPercentage: 0.4
                    }]

                }
            }
        });



    }
});

//Revenue Chart js homepage data.
$(function () {
    var endpoint = '/api/course/revenue/data/'
    var defaultData = []
    var labels = [];
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            course = data.course
            totalRevenue = data.total_revenue
            setChart()
        },
        error: function (error_data) {
            console.log("error")
            //                console.log(error_data)
        }
    })

    function setChart() {
        var ctx2 = document.getElementById("revenue-chart");
        var myChart = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: course,
                datasets: [{
                    label: '# revenue in course',
                    data: totalRevenue,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 0.5
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            display:true,
                            // Include a dollar sign in the ticks
                            callback: function(value, index, values) {
                                return 'Rs' + value;
                            }
                        },
                         scaleLabel: {
                            display: true,
                            labelString: 'Total Revenue in rupees'
                          }
                    }],
                     xAxes: [{
                        barPercentage: 0.4
                    }]
                }
            }
        });



    }
});