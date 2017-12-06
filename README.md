# 손놈봇 (discord_py-sonnom)

[![Englsh](https://img.shields.io/badge/Language-English-red.svg)](README.md)
![Korean](https://img.shields.io/badge/Language-Korean-lightgrey.svg)

- Discord 채널 관리 명령어 봇

## 기능
- /moveall : 현재 Voice채널 사용자를 채널로 이동시킵니다.

## 요구사항
- Python 3.5 later

## How to use
- In your project's editor settings, make sure your asset serialization mode is set to "Force Text". This is absolutely crucial.
- For each scene you have create a prefab containing all game objects in that scene. The reason for that is that scenes cannot be forced to use a text format. So instead the converter goes through all prefabs and fixes them.
- Throw your project's assets folder into the "Put your assets folder here" folder.
- Run the tool and press enter to start converting.
- Your assets folder inside "Put your assets folder here" is now converted. So go ahead and delete your project's old assets and library folders and then copy your new assets folder over there.
- Run your project in Unity 5.4 and tell it to continue even though the project versions mismatch.

## Known issues
- Particle systems that use the Sub module will have their Sub module reset.
- If the project was originally created before 5.5, then any textures\sprites added to the project after it was upgraded to 5.5 will need to have their settings reset. It's as simple as changing the texture type to something else and then back to what it's meant to be. Just make sure the mipmaps\compression settings are set to what you expect them to be.
- Any image\button components added while the project version was 5.5 will be corrupted. You'll either need to remove and add those components manually or upgrade the source code to fix the missing GUIDs on those components(read MykolaDenysenko's comment on this)


## Source
- discord.py : https://github.com/Rapptz/discord.py
