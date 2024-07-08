import subprocess
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster

# Function to automate SQLMap with captured HTTP requests from mitmproxy

def automate_sqlmap_with_mitmproxy():
# SQLMap command template
    sqlmap_command = ["sqlmap", "-r", "-", "--batch", "--level=5", "--risk=3"]

    try:
    # Start mitmproxy to capture HTTP traffic
        mitmproxy_opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
        m = DumpMaster(options=mitmproxy_opts)
        config = proxy.config.ProxyConfig(mitmproxy_opts)
        m.server = proxy.server.ProxyServer(config)
        m.addons.add(DumpMaster)

        # Start mitmproxy in a separate thread
        t = threading.Thread(target=m.run)
        t.start()

        # Process captured requests in real-time
        while True:
            # Assuming mitmproxy captures and saves requests to 'captured_request.txt' 
            with open('captured_request.txt', 'r') as file:
                request_data = file.read()
                # Run SQLMap using subprocess
                process = subprocess.Popen(sqlmap_command, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=request_data.encode())

                # Print SQLMap output
                print("SQLMap output:")
                print(stdout.decode())

                if stderr:
                    print("Error occurred:")
                    print(stderr.decode())

            # Sleep for a while before checking for new requests
            time.sleep(5)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Stop mitmproxy
        m.shutdown()
        t.join()

# Start the automation process
automate_sqlmap_with_mitmproxy()