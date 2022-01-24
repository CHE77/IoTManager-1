#pragma once
#include "Global.h"

#ifdef STANDARD_WEB_SERVER
extern void standWebServerInit();
extern bool handleFileRead(String path);
extern String getContentType(String filename);
#ifdef REST_FILE_OPERATIONS
extern void handleFileUpload();
extern void handleFileDelete();
extern void handleFileCreate();
extern void handleFileList();
#endif
#endif

#ifdef STANDARD_WEB_SOCKETS
extern void standWebSocketsInit();
extern void webSocketEvent(uint8_t num, WStype_t type, uint8_t* payload, size_t length);
#ifdef ESP32
extern void hexdump(const void* mem, uint32_t len, uint8_t cols);
#endif
#endif

void sendFileToWs3(const String& filename, uint8_t num);
void sendFileToWs4(const String& filename, uint8_t num);
void sendFileToWs5(const String& filename, uint8_t num);