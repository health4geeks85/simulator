import time
import random
import base64
import datetime
import sys
from colorama import init, Fore, Style
import win32api
import signal


nowFormat = '%Y-%m-%dT%H:%M:%S.%fZ'
dateFormat = '%Y-%m-%d'
timeFormat = '%H:%M:%S'

OPENING_TEXT = '''
*****************************************************************************************************************
*   _____ _____            _______ _____            _   _    _____ ____  __  __ _____        _   ___     _ _    *
*  / ____|_   _|   /\     |__   __|  __ \     /\   | \ | |  / ____/ __ \|  \/  |  __ \ /\   | \ | \ \   / /     *
* | |  __  | |    /  \       | |  | |__) |   /  \  |  \| | | |   | |  | | \  / | |__) /  \  |  \| |\ \_/ /      * 
* | | |_ | | |   / /\ \      | |  |  _  /   / /\ \ | . ` | | |   | |  | | |\/| |  ___/ /\ \ | . ` | \   /       * 
* | |__| |_| |_ / ____ \     | |  | | \ \  / ____ \| |\  | | |___| |__| | |  | | |  / ____ \| |\  |  | |        * 
*  \_____|_____/_/    \_\    |_|  |_|  \_\/_/    \_\_| \_|  \_____\____/|_|  |_|_| /_/    \_\_| \_|  |_|        *
*                                                                                                               * 
*                                                                                                               *
*      COPYRIGHT (c) 2017 GIA TRAN COMPANY                                                                      *
*      All rights reserved.                                                                                     *
*      BLOCKCHAIN PROJECT                                                                                       *                         
*                                                                                                               *                         
*  * Redistributions of source code must retain the above copyright notice, this                                *                        
*    list of conditions and the following disclaimer.                                                           *
*                                                                                                               *
*  * Redistributions in binary form must reproduce the above copyright notice,                                  *
*    this list of conditions and the following disclaimer in the documentation                                  *
*    and/or other materials provided with the distribution.                                                     *
*                                                                                                               *
*  * Neither the name of the copyright holders, nor those of its contributors                                   *
*    may be used to endorse or promote products derived from this software without                              *
*    specific prior written permission.                                                                         *
*                                                                                                               *
*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND                              *
*  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED                                *
*  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE                                       *
*  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE                                 *                           
*  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL                                   *   
*  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR                                   *
*  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER                                   *
*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,                                *
*  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE                                *
*  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                         *
*****************************************************************************************************************
'''
EXIT_BOOL = False

def exitGracefully(signum, frame):
    global EXIT_BOOL
    print(Fore.RED + "Quitting....")
    time.sleep(0.3)
    EXIT_BOOL = True
    return True

def winExit(*args):
    global EXIT_BOOL
    print(Fore.RED + "Quitting....")
    time.sleep(0.3)
    EXIT_BOOL = True
    return True


def registerSignals():
    signal.signal(signal.SIGINT, exitGracefully)
    signal.signal(signal.SIGTERM, exitGracefully)
    signal.signal(signal.SIGABRT, exitGracefully)
    signal.signal(signal.SIGSEGV, exitGracefully)
    signal.signal(signal.SIGILL, exitGracefully)
    signal.signal(signal.SIGFPE, exitGracefully)
    win32api.SetConsoleCtrlHandler(winExit, True)

def display(path):
    print(Fore.RED)
    print(OPENING_TEXT)
    print(Style.RESET_ALL)
    print("Initializing.....")
    time.sleep(2)

    # register exit signals
    registerSignals()

    with open(path, 'rb') as f:
        content = f.read()
    lines = base64.b64decode(content).decode()
    buf = list(lines.split('\n'))
    while not EXIT_BOOL:
        if not buf:
            buf = list(lines.split('\n'))
        time.sleep(random.randint(0, 9)/9)
        now = datetime.datetime.now()
        line = buf.pop()
        print(line.format(now=now.strftime(nowFormat),
                          date=now.strftime(dateFormat),
                          time=now.strftime(timeFormat)))

if __name__ == "__main__":
    init()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'orderer':
            display('orderer.bin')
        else:
            display('peer.bin')
    else:
        display('orderer.bin')
