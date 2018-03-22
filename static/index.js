var width = 650;
var height = 400;
var color = ["#ae0e11", "#ae0ea8", "#240eae", "#37ae0e", "#ae770e", "#029382"];
d3.select("#rect").append("svg").attr("class", "rect_svg").attr("width", width);
d3.select("#line").append("svg").attr("class", "line_svg").attr("width", width + 20).attr("height", height + 50);

function sort_mvp(jsondata) {
    jsondata.sort(function (a, b) {
        return b.mvp - a.mvp
    });
}

function sort_stl(jsondata) {
    jsondata.sort(function (a, b) {
        return b.stl_16 - a.stl_16
    });
}

function sort_trb(jsondata) {
    jsondata.sort(function (a, b) {
        return b.trb_16 - a.trb_16
    });
}

function sort_ast(jsondata) {
    jsondata.sort(function (a, b) {
        return b.ast_16 - a.ast_16
    });
}

function sort_css(i) {
    if (i.innerText == "效率值") {
        return "#029382";
    }
    if (i.innerText == "场均助攻") {
        return color[0];
    }
    if (i.innerText == "场均盖帽") {
        return color[1]
    }
    if (i.innerText == "场均得分") {
        return color[2]
    }
    if (i.innerText == "场均抢断") {
        return color[3];
    }
    if (i.innerText == "场均篮板") {
        return color[4];
    }
}

function GetPlayerName(jsondata) {
    $('.name').remove();
    var list = d3.select("#players");
    list.selectAll(".name")
        .data(jsondata)
        .enter()
        .append("li")
        .attr("class", "name")
        .text(function (d) {
            return d.player
        })
        .on("click", function () {
            console.log(this);
            Player_massage(this);
            $(this).css("color", "white");
            $(this).css("background-color", Player_css(this));
            $(".name").not(this).css("color", "black");
            $(".name").not(this).css("background-color", "white");
            Rect();
            updata_rect(this)
        })
}

function sort_psg(jsondata) {
    jsondata.sort(function (a, b) {
        return b.psg_16 - a.psg_16
    });
}

function sort_blk(jsondata) {
    jsondata.sort(function (a, b) {
        return b.blk_16 - a.blk_16
    });
}

function Player_css(i) {
    var datas = [i.__data__.ast_16[0], i.__data__.blk_16[0], i.__data__.psg_16[0], i.__data__.stl_16[0], i.__data__.trb_16[0], i.__data__.mvp[0]];
    var max = datas[0];
    for (var p = 0; p < datas.length; p++) {
        if (max <= datas[p]) {
            max = datas[p];
        }
    }
    for (var q = 0; q < datas.length; q++) {
        if (max == datas[q]) {
            return color[q];
        }
    }
}

function sort_name(jsondata, q) {
    if (q == "效率值") {
        sort_mvp(jsondata);
        GetPlayerName(jsondata)
    }
    else if (q == "场均得分") {
        sort_psg(jsondata);
        GetPlayerName(jsondata)
    }
    else if (q == "场均盖帽") {
        sort_blk(jsondata);
        GetPlayerName(jsondata)
    }
    else if (q == "场均抢断") {
        sort_stl(jsondata);
        GetPlayerName(jsondata)
    }
    else if (q == "场均篮板") {
        sort_trb(jsondata);
        GetPlayerName(jsondata)
    }
    else if (q == "场均助攻") {
        sort_ast(jsondata);
        GetPlayerName(jsondata)
    }
}

function GetLogo(i) {
    $("img").remove();
    d3.select("#logo")
        .append("img")
        .attr("src", i);
}

function Player_massage(i) {
    d3.select("#title").text(i.__data__.player[0]);
    d3.select("#next_title").text("年龄:" + i.__data__.age[0] + " | " + "位置:" + i.__data__.pos[0] + " | " + "比赛数:" + i.__data__.g[0])

}

function updata_rect(i) {
    var datasets = [i.__data__.ast_16[0], i.__data__.blk_16[0], i.__data__.psg_16[0], i.__data__.stl_16[0], i.__data__.trb_16[0]];
    d3.selectAll(".rects")
        .data(datasets)
        .transition()
        .duration(500)
        .ease("linear")
        .attr("height",function (d,i) {
            return datasets[i]*2+5
        })
}

function Rect() {
    var xScale = d3.scale.ordinal()
        .domain([0, 1, 2, 3, 4])
        .rangeRoundBands([0, 550]);
    var datasets = [1, 1, 1, 1, 1];
    var name = ["场均助攻数", "场均盖帽数", "场均得分", "场均抢断数", "场均篮板球数"];
    var Rect = d3.select(".rect_svg");
    Rect.selectAll(".rects")
        .data(datasets)
        .enter()
        .append("rect")
        .attr("class", "rects")
        .attr("transform", "translate(40,40)")
        .attr("fill", function (d, i) {
            return color[i]
        })
        .attr("x", function (d, i) {
            return xScale(i)
        })
        .attr("width", 85)
        .attr("height", function (d, i) {
            return datasets[i] * 2 + 5
        })
        .on("click",function () {
            console.log(this)
        });

    Rect.selectAll(".text1")
        .data(name)
        .enter()
        .append("text")
        .attr("class", "text1")
        .attr("transform", "translate(40,30)")
        .attr("x", function (d, i) {
            return xScale(i)
        })
        .text(function (d) {
            return d
        })
        .attr("font_size", "20px")

}

function updata_line(i) {
    switch (i.attributes.fill.value) {
        case color[0]:
            dataset = [i.__data__.ast_12[0], i.__data__.ast_13[0], i.__data__.ast_14[0], i.__data__.ast_15[0], i.__data__.ast_16[0]];
            tag = "场均助攻数";
            colors = color[0];
            break;
        case color[1]:
            dataset = [i.__data__.blk_12[0], i.__data__.blk_13[0], i.__data__.blk_14[0], i.__data__.blk_15[0], i.__data__.blk_16[0]];
            tag = "场均盖帽数";
            colors = color[1];
            break;
        case color[2]:
            dataset = [i.__data__.psg_12[0], i.__data__.psg_13[0], i.__data__.psg_14[0], i.__data__.psg_15[0], i.__data__.psg_16[0]];
            tag = "场均得分";
            colors = color[2];
            break;
        case color[3]:
            dataset = [i.__data__.stl_12[0], i.__data__.stl_13[0], i.__data__.stl_14[0], i.__data__.stl_15[0], i.__data__.stl_16[0]];
            tag = "场均抢断数";
            colors = color[3];
            break;
        case color[4]:
            dataset = [i.__data__.trb_12[0], i.__data__.trb_13[0], i.__data__.trb_14[0], i.__data__.trb_15[0], i.__data__.trb_16[0]];
            tag = "场均篮板球数";
            colors = color[4];
            break;
    }
}

function Line() {
    var svg = d3.select(".line_svg");
    var dataset = [0,0,0,0,0];

    console.log(dataset);

    var x = d3.scale.ordinal()
        .domain([2013, 2014, 2015, 2016, 2017])
        .rangeRoundBands([0, width - 30]);

    var y = d3.scale.linear()
        .domain([0, d3.max(dataset, function (d) {
            return d;
        })])
        .range([height - 30, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var gxAxis = svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(40,400)")
        .call(xAxis)
        .append("text")
        .attr("x", 620)
        .attr("y", 20)
        .style("text-anchor", "end")
        .text("年份");

    var gyAxis = svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(40,30)")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 17)
        .style("text-anchor", "end")
        .text(tag);

    var line = d3.svg.line()
        .x(function (d, i) {
            return x(i + 2013);
        })
        .y(function (d) {
            return y(d);
        });

    svg.append("path")
        .attr("class", "line_path")
        .transition()
        // .duration(1000)
        // .ease("linear")
        .attr("d", line(dataset))
        .attr("transform", "translate(40,30)")
        .attr("fill", "none")
        .attr("stroke", black)
        .attr("stroke-width", "2px");

    var circle = svg.selectAll(".circle")
        .data(dataset)
        .enter()
        .append("circle")
        .attr("r", 5)
        .transition()
        // .duration(1000)
        // .ease("linear")
        .attr("cx", function (d, i) {
            return x(i + 2013);
        })
        .attr("cy", function (d) {
            return y(d)
        })
        .attr("class", "line_circle")
        .attr("transform", "translate(40,30)")
        .attr("fill", "white")
        .attr("stroke", colors)
        .attr("stroke-width", "2px")
}

d3.selectAll(".nba")
    .on("click", function () {
        console.log(this.innerText);
        switch (this.innerText) {
            case "华盛顿奇才":
                d3.json(/was/, function (error, jsondata) {
                    if (error)
                        console.log(error);
                    console.log(jsondata);
                    d3.select("#was")
                        .style("background-color", "dodgerblue")
                        .style("color", "white");
                    sort_mvp(jsondata);
                    GetPlayerName(jsondata);
                    $(".sort:first").css("background-color", color[5]);
                    $(".sort:first").css("color", "white");
                    GetLogo("http://mat1.gtimg.com/sports/nba/logo/1602/27.png");
                    d3.selectAll(".sort")
                        .on("click", function () {
                            $(this).css("color", "white");
                            $(this).css("background-color", sort_css(this));
                            $(".sort").not(this).css("color", "black");
                            $(".sort").not(this).css("background-color", "white");
                            sort_name(jsondata, this.innerHTML)
                        })
                })
        }
    });
