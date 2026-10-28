import urllib.request
import urllib.error
import time
from database import save_result

def monitor_api(url):
    try:
        start= time.perf_counter()
        with urllib.request.urlopen( url, timeout=5) as response:
            status_code = response.status
        end=time.perf_counter()
        response_time=round((end-start)*1000,2)
        display_result(status_code,response_time, url)
        return url, status_code, response_time, None
        
    except urllib.error.HTTPError as error:
        with error:
            status_code=error.code

        end=time.perf_counter()
        response_time=round((end-start)*1000,2)
        display_result(status_code,response_time, url)
        return url, status_code, response_time, None
        
    except urllib.error.URLError as error:
        end=time.perf_counter()
        response_time=round((end-start)*1000,2)
        
        if isinstance(error.reason,TimeoutError):
            print(url,"\n Request timed out")
            error_type= "TIMEOUT"
        else:
            print("checking: ", url, "\n","Network error detected",'\n',error.reason)
            error_type= "NETWORK_ERROR"
        return url, None, response_time, error_type
    except TimeoutError:
        end=time.perf_counter()
        error_type= "TIMEOUT"
        response_time=round((end-start)*1000,2)
        print(url,"\n Request timed out")
        return url, None, response_time, error_type
    
def check_status(status_code):

    if 200<= status_code<300:
        return True

    else:
       return False

def display_result(status_code, response_time, url):
    result = check_status(status_code)
    if result:
        print("checking: ", url, "\n","API is healthy")
        

    else:
        print("checking: ", url, "\n","API error detected")
        
    print("Response time: ", response_time,"ms")

    

if __name__ == "__main__":
    urls = [
    "https://github.com",
    "https://httpbin.org/status/404",
    "https://gitlllhub.com"
    ]
    for url in urls:
        print("Checking", url)
        result = monitor_api(url)
        if result is not None:
            save_result(result[0],result[1],result[2],result[3])
            print("Returned:", result)

    