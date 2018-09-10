/**
 * Created by liubo on 2018/8/16.
 */
'use strict'
var express = require('express');
var router = express.Router();

var AV = require('leanengine');

/**
 * /all 按照时间顺序从小到大排列
 * /2018
 * /2017
 * /2016
 * /last6month
 * /last1year
 */

router.get('/all', function (req, res) {
    AV.Cloud.run('car_all').then(function (data) {
        res.json({status: 'ok', type: 'all', 'result': data});
    }, function (err) {
    });

});

router.get('/2018', function (req, res) {
    var params = {year: 2018};
    AV.Cloud.run('car_year', params).then(function (data) {
        res.json({status: 'ok', type: '2018', 'result': data});
    }, function (err) {
    });
});

router.get('/2017', function (req, res) {
    var params = {year: 2017};
    AV.Cloud.run('car_year', params).then(function (data) {
        res.json({status: 'ok', type: '2017','result': data});
    }, function (err) {
    });
});

router.get('/2016', function (req, res) {
    var params = {year: 2016};
    AV.Cloud.run('car_year', params).then(function (data) {
        res.json({status: 'ok', type: '2016','result': data});
    }, function (err) {
    });
});


router.get('/2015', function (req, res) {
    var params = {year: 2015};
    AV.Cloud.run('car_year', params).then(function (data) {
        res.json({status: 'ok', type: '2015','result': data});
    }, function (err) {
    });
});


router.get('/last6month', function (req, res) {
    AV.Cloud.run('car_last6month').then(function (data) {
        res.json({status: 'ok', type: 'last6month','result': data});
    }, function (err) {
    });
});


router.get('/last1year', function (req, res) {
    AV.Cloud.run('car_last1year').then(function (data) {
        res.json({status: 'ok', type: 'last1year','result': data});
    }, function (err) {
    });
});


module.exports = router;
