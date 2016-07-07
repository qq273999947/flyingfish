package com.flyingfish;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Created by yuxiang on 16-7-7.
 */
@Controller
@RequestMapping("/")
public class HelloWorld {

    private static final Logger LOGGER = LoggerFactory.getLogger(HelloWorld.class);

    @RequestMapping("hello")
    public String printHello() {
        return "index";
    }

}
