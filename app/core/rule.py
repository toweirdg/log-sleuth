RULES = {
    "timeout":{
        "severity":"CRITICAL",
        "action":"Restart service"
    },
    "connection refused":{
        "severity":"ERROR",
        "action":"Check database"
    }
}
