#include "pch.h"
#include "BuiltInFunc.h"
#include <limits.h>

/* �r���h���� C4273 ���o�邯�ǁA���삵�Ă�̂ŋC�ɂ��Ȃ��B
 * �C�ɂȂ�Ȃ�v���W�F�N�g�ݒ�ŗ}������Ηǂ��Ǝv���B
 */

// �l�n��+�l�߂�
int sum_int(int x, int y)
{
	return x + y;
}

// �Q�Ɠn��
void get_int_max(int *x)
{
	*x = INT_MAX;
}

// ������ݒ�
void get_string(char* str, int length)
{
	strcpy_s(str, length, "Hello World! (set from C++Lib)");
}

// �\���̂̎Q�Ɠn��
void get_struct(channels* ch)
{
	ch->b = 0x00;
	ch->g = 0x80;
	ch->r = 0xff;
}
