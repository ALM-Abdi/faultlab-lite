import sqlite3

def show_statistics():
    conn=sqlite3.connect("faultlab.db")
    cur=conn.cursor()
    cur.execute("""
    SELECT 
        url, 
        COUNT(*), 
        AVG(response_time_ms), 
        SUM (
            CASE 
                WHEN status_code>= 200 AND status_code<300 THEN 1 
                ELSE 0
            END),
        AVG(
            CASE 
                WHEN status_code>= 200 AND status_code<300 THEN response_time_ms 
                ELSE NULL
            END)
            
    FROM api_checks GROUP BY url
    """)

    api_averages=cur.fetchall()
    for avg_api in api_averages:
        avg_url=avg_api[0]
        checks= avg_api[1]
        avg_time=round(avg_api[2],2)
        success_api=avg_api[3]
        if checks !=0:
            success_rate = (success_api/checks)*100
        else:
            success_rate=0
        avg_success_time = avg_api[4]

        if avg_success_time is not None:
            avg_success_time=f"{round(avg_success_time,2)} ms"
        else:
            avg_success_time="N/A"
        print("API:", avg_url, "\nChecks: ",checks , "\nSuccessful checks: ", success_api, 
            "\nSuccess rate: ",round(success_rate,1),"%", 
            "\nAverage response time:", avg_time, "ms","\nAverage successful response time: ", avg_success_time )
    conn.close()

