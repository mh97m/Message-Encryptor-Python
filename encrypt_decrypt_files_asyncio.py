#!/usr/bin/env python
import os
import sys
import time
import argparse
from cryptography.fernet import Fernet
import asyncio


class EncryptorDecryptor:

    def __init__(self) -> None:
        args = self.getArgs()
        self.mode = args.mode
        self.directory = args.dir



        # self.async_loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(self.async_loop)

    def getArgs(self):
        parser = argparse.ArgumentParser(
            description='Encrypt or decrypt all files in a directory')
        parser.add_argument('--mode', choices=[
                            'encrypt', 'decrypt'], help='Mode to run the program in (encrypt or decrypt)')
        parser.add_argument('--dir', help='Directory to process')
        return parser.parse_args()

    def encryptData(self, file_name):
        with open(file_name, 'rb') as file:
            file_data = file.read()
        print(file_data)
        with open(file_name, 'wb') as new_file:
            new_file.write(file_data)

    def decryptData(self, file_name):
        with open(file_name, 'rb') as file:
            file_data = file.read()
        print(file_data)
        with open(file_name, 'wb') as new_file:
            new_file.write(file_data)

    async def execute(self,file_name):
        if self.mode == 'encrypt':
            self.encryptData(file_name)
        elif self.mode == 'decrypt':
            self.decryptData(file_name)

    async def executeAll(self):
        for root, _, files in os.walk(self.directory):
            tasks = []
            for file in files:
                file_name = os.path.join(root, file)
                tasks.append(asyncio.ensure_future(self.execute(file_name)))

            await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.monotonic()
    asyncio.run(EncryptorDecryptor().executeAll())
    end = time.monotonic()
    print(f"Operation completed in: {end-start} seconds")
