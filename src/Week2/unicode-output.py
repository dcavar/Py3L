#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

print("some åäö-string cvrčak Ʒɺʃɳ Жиба こんにちは。 また明日。 幸会 你好 안녕하세요 안녕히 주무셨어요? 안녕하세요? مرحبا سلام إشتقت إليك كثيرا")
