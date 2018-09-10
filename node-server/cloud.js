var AV = require('leanengine');

/**
 * 一个简单的云代码方法
 */
AV.Cloud.define('hello', function (request) {
    return 'Hello world!';
});


/**
 * /all 按照时间顺序从小到大排列
 * /2018
 * /2017
 * /2016
 * /last6month
 * /last1year
 */

var TABLE_NAME = 'SZ_CAR_BID_PRICE';

function getResults(query) {
    return query.find().then(function (items) {
        var results = [];
        for (var i = 0; i < items.length; i++) {
            var result = items[i];
            results.push({"year": result.get("year"), 'month': result.get("month")});
        }

        return results;
    }, function (error) {
        console.log("error", error);
        return {"error": "internal error!"};
    });
}


AV.Cloud.define('car_all', function (request) {
    var query = new AV.Query(TABLE_NAME);
    query.descending('year');
    return getResults(query);
});

AV.Cloud.define('car_year', function (request) {
    var year = request.params.year;

    var query = new AV.Query(TABLE_NAME);
    query.descending('month');
    query.equalTo('year', year);
    return getResults(query);

});


AV.Cloud.define('car_last6month', function (request) {
    var query = new AV.Query(TABLE_NAME);
    query.descending('year');
    query.limit(6);
    return getResults(query);
});


AV.Cloud.define('car_last1year', function (request) {
    var query = new AV.Query(TABLE_NAME);
    query.descending('year');
    query.limit(12);
    return getResults(query);
});