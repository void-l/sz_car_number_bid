/**
 * Created by liubo on 2018/8/16.
 */
'use strict'
var express = require('express');
var router = express.Router();

/**
 * /all
 * /2018
 * /2017
 * /2016
 * /last6month
 * /last1year
 */

router.get('/all', function(req, res){
    res.json({'year': 2018, 'month': 7});
});




module.exports = router;
