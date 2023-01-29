$( document ).ready(function() {
    console.log( "ready!" );

    const {
        host, hostname, href, origin, pathname, port, protocol, search
    } = window.location

    $("a[href='"+ pathname + "']").addClass("active")

    $(".projectTitle").each( function (i, el) {
        $(el).html("Loading....").load("/project?id=" + $(el).attr("data-id"))
    });

    $(".projectInfo").each( function (i, el) {
        $(el).html("Loading....").load("/project/info?id=" + $(el).attr("data-id"))
    });


    $(".pipelineInfo").each( function (i, el) {
        $(el).html("Loading....").load("/pipelines/latest?id=" + $(el).attr("data-id"),
            function (res, stat) {
                if ( res.includes("success") ) {
                    $("#box-" + $(el).attr("data-id")).toggleClass('bg-dark bg-success');
                } else if ( res.includes("failed") ) {
                    $("#box-" + $(el).attr("data-id")).toggleClass('bg-dark bg-danger');
                } else if ( res.includes("canceled") ) {
                    $("#box-" + $(el).attr("data-id")).toggleClass('bg-dark bg-warning');
                } else if ( res.includes("running") ) {
                    $("#box-" + $(el).attr("data-id")).toggleClass('bg-dark bg-info');
                }
            })
    });

});