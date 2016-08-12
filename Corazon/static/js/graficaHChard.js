/**
 * Created by raquel on 23/07/16.
 */

$(function() {
            $.noConflict();
            Highcharts.setOptions({
                global : {
                    useUTC : false
                }
            });

            // Create the chart
            $('#contenedor').highcharts('StockChart', {
                chart : {
                    events : {
                        load : function () {
                            // set up the updating of the chart each second
                            var series = this.series[0];
                            setInterval(function () {
                                $.post( "/mapa/api/lps.dat",{ id_dispo:'12345'},
                                        function( data ) {
                                            //$( ".result" ).html( data );
                                            console.log(data);
                                            var x = (new Date()).getTime(), // current time
                                                y = parseInt(data);
                                            series.addPoint([x, y], true, true);
                                        }
                                );
                            }, 1000);
                        }
                    }
                },

                rangeSelector: {
                    buttons: [{
                        count: 1,
                        type: 'minute',
                        text: '1M'
                    }, {
                        count: 5,
                        type: 'minute',
                        text: '5M'
                    }, {
                        type: 'all',
                        text: 'All'
                    }],
                    inputEnabled: false,
                    selected: 0
                },

                title : {
                    text : 'Grafica Ritmo Cardiaco'
                },

                exporting: {
                    enabled: false
                },

                series : [{
                    name : 'BPM',
                    data : (function () {
                        // generate an array of random data
                        var data = [], time = (new Date()).getTime(), i;

                        for (i = -999; i <= 0; i += 1) {
                            data.push([
                                2
                            ]);
                        }
                        return data;
                    }())
                }]
    });

});