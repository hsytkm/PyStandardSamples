#pragma once

// pch.h ‚É‘‚¢‚½•û‚ªƒXƒbƒLƒŠ‚·‚é‚ª‰Â‹‰»‚Ì‚½‚ß
#ifdef TESTLIB_EXPORTS
#define TESTLIB_API extern "C" __declspec(dllexport)
#else
#define TESTLIB_API extern "C" __declspec(dllimport)
#endif

struct channels {
    unsigned char b;
    unsigned char g;
    unsigned char r;
};

TESTLIB_API int sum_int(int, int);
TESTLIB_API void get_int_max(int*);
TESTLIB_API void get_string(char*, int );
TESTLIB_API void get_struct(channels*);
