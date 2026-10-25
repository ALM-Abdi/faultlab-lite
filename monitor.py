import urllib.request
import urllib.error
import time

def monitor_api(url):
    try:
        start= time.perf_counter()
        with urllib.request.urlopen( url, timeout=5) as response:
            status_code = response.status
        end=time.perf_counter()
        display_result(status_code,round((end-start)*1000,2), url)
    
    except urllib.error.HTTPError as error:
        with error:
            status_code=error.code

        end=time.perf_counter()
        display_result(status_code,round((end-start)*1000,2), url)
        
    except urllib.error.URLError as error:
        end=time.perf_counter()
        if isinstance(error.reason,TimeoutError):
            print(url,"\n Request timed out")
        else:
            print("checking: ", url, "\n","Network error detected",'\n',error.reason)

    except TimeoutError:
        print(url,"\n Request timed out")
    
    
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
    monitor_api("https://github.com")
    monitor_api("https://httpbin.org/status/404")
    monitor_api("https://example.invalid")