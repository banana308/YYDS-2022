import requests
import json
import threading
import _thread
import datetime
import xlwt
import openpyxl
import time
import datetime
import random
import random
from concurrent.futures import ThreadPoolExecutor


num01="bDuFCeshi0400"
num=['a1dx02030f', 'a1dx02030g', 'a1dx02030h', 'a1dx02030i', 'a1dx02030j', 'a1dx02030k', 'a1dx02030l', 'a1dx02030m', 'a1dx02030n', 'a1dx02030o', 'a1dx02030p', 'a1dx02030q', 'a1dx02030r', 'a1dx02030s', 'a1dx02030t', 'a1dx02030u', 'a1dx02030v', 'a1dx02030w', 'a1dx02030x', 'a1dx02030y', 'a1dx02030z', 'a1dx02031a', 'a1dx02031b', 'a1dx02031c', 'a1dx02031d', 'a1dx02031e', 'a1dx02031f', 'a1dx02031g', 'a1dx02031h', 'a1dx02031i', 'a1dx02031j', 'a1dx02031k', 'a1dx02031l', 'a1dx02031m', 'a1dx02031n', 'a1dx02031o', 'a1dx02031p', 'a1dx02031q', 'a1dx02031r', 'a1dx02031s', 'a1dx02031t', 'a1dx02031u', 'a1dx02031v', 'a1dx02031w', 'a1dx02031x', 'a1dx02031y', 'a1dx02031z', 'a1dx02032a', 'a1dx02032b', 'a1dx02032c', 'a1dx02032d', 'a1dx02032e', 'a1dx02032f', 'a1dx02032g', 'a1dx02032h', 'a1dx02032i', 'a1dx02032j', 'a1dx02032k', 'a1dx02032l', 'a1dx02032m', 'a1dx02032n', 'a1dx02032o', 'a1dx02032p', 'a1dx02032q', 'a1dx02032r', 'a1dx02032s', 'a1dx02032t', 'a1dx02032u', 'a1dx02032v', 'a1dx02032w', 'a1dx02032x', 'a1dx02032y', 'a1dx02032z', 'a1dx02033a', 'a1dx02033b', 'a1dx02033c', 'a1dx02033d', 'a1dx02033e', 'a1dx02033f', 'a1dx02033g', 'a1dx02033h', 'a1dx02033i', 'a1dx02033j', 'a1dx02033k', 'a1dx02033l', 'a1dx02033m', 'a1dx02033n', 'a1dx02033o', 'a1dx02033p', 'a1dx02033q', 'a1dx02033r', 'a1dx02033s', 'a1dx02033t', 'a1dx02033u', 'a1dx02033v', 'a1dx02033w', 'a1dx02033x', 'a1dx02033y', 'a1dx02033z', 'a1dx02034a', 'a1dx02034b', 'a1dx02034c', 'a1dx02034d', 'a1dx02034e', 'a1dx02034f', 'a1dx02034g', 'a1dx02034h', 'a1dx02034i', 'a1dx02034j', 'a1dx02034k', 'a1dx02034l', 'a1dx02034m', 'a1dx02034n', 'a1dx02034o', 'a1dx02034p', 'a1dx02034q', 'a1dx02034r', 'a1dx02034s', 'a1dx02034t', 'a1dx02034u', 'a1dx02034v', 'a1dx02034w', 'a1dx02034x', 'a1dx02034y', 'a1dx02034z', 'a1dx02035a', 'a1dx02035b', 'a1dx02035c', 'a1dx02035d', 'a1dx02035e', 'a1dx02035f', 'a1dx02035g', 'a1dx02035h', 'a1dx02035i', 'a1dx02035j', 'a1dx02035k', 'a1dx02035l', 'a1dx02035m', 'a1dx02035n', 'a1dx02035o', 'a1dx02035p', 'a1dx02035q', 'a1dx02035r', 'a1dx02035s', 'a1dx02035t', 'a1dx02035u', 'a1dx02035v', 'a1dx02035w', 'a1dx02035x', 'a1dx02035y', 'a1dx02035z', 'a1dx02036a', 'a1dx02036b', 'a1dx02036c', 'a1dx02036d', 'a1dx02036e', 'a1dx02036f', 'a1dx02036g', 'a1dx02036h', 'a1dx02036i', 'a1dx02036j', 'a1dx02036k', 'a1dx02036l', 'a1dx02036m', 'a1dx02036n', 'a1dx02036o', 'a1dx02036p', 'a1dx02036q', 'a1dx02036r', 'a1dx02036s', 'a1dx02036t', 'a1dx02036u', 'a1dx02036v', 'a1dx02036w', 'a1dx02036x', 'a1dx02036y', 'a1dx02036z', 'a1dx02037a', 'a1dx02037b', 'a1dx02037c', 'a1dx02037d', 'a1dx02037e', 'a1dx02037f', 'a1dx02037g', 'a1dx02037h', 'a1dx02037i', 'a1dx02037j', 'a1dx02037k', 'a1dx02037l', 'a1dx02037m', 'a1dx02037n', 'a1dx02037o', 'a1dx02037p', 'a1dx02037q', 'a1dx02037r', 'a1dx02037s', 'a1dx02037t', 'a1dx02037u', 'a1dx02037v', 'a1dx02037w', 'a1dx02037x', 'a1dx02037y', 'a1dx02037z', 'a1dx02038a', 'a1dx02038b', 'a1dx02038c', 'a1dx02038d', 'a1dx02038e', 'a1dx02038f', 'a1dx02038g', 'a1dx02038h', 'a1dx02038i', 'a1dx02038j', 'a1dx02038k', 'a1dx02038l', 'a1dx02038m', 'a1dx02038n', 'a1dx02038o', 'a1dx02038p', 'a1dx02038q', 'a1dx02038r', 'a1dx02038s', 'a1dx02038t', 'a1dx02038u', 'a1dx02038v', 'a1dx02038w', 'a1dx02038x', 'a1dx02038y', 'a1dx02038z', 'a1dx02039a', 'a1dx02039b', 'a1dx02039c', 'a1dx02039d', 'a1dx02039e', 'a1dx02039f', 'a1dx02039g', 'a1dx02039h', 'a1dx02039i', 'a1dx02039j', 'a1dx02039k', 'a1dx02039l', 'a1dx02039m', 'a1dx02039n', 'a1dx02039o', 'a1dx02039p', 'a1dx02039q', 'a1dx02039r', 'a1dx02039s', 'a1dx02039t', 'a1dx02039u', 'a1dx02039v', 'a1dx02039w', 'a1dx02039x', 'a1dx02039y', 'a1dx02039z', 'a1dx0203a0', 'a1dx0203a1', 'a1dx0203a2', 'a1dx0203a3', 'a1dx0203a4', 'a1dx0203a5', 'a1dx0203a6', 'a1dx0203a7', 'a1dx0203a8', 'a1dx0203a9', 'a1dx0203b0', 'a1dx0203b1', 'a1dx0203b2', 'a1dx0203b3', 'a1dx0203b4', 'a1dx0203b5', 'a1dx0203b6', 'a1dx0203b7', 'a1dx0203b8', 'a1dx0203b9', 'a1dx0203c0', 'a1dx0203c1', 'a1dx0203c2', 'a1dx0203c3', 'a1dx0203c4', 'a1dx0203c5', 'a1dx0203c6', 'a1dx0203c7', 'a1dx0203c8', 'a1dx0203c9', 'a1dx0203d0', 'a1dx0203d1', 'a1dx0203d2', 'a1dx0203d3', 'a1dx0203d4', 'a1dx0203d5', 'a1dx0203d6', 'a1dx0203d7', 'a1dx0203d8', 'a1dx0203d9', 'a1dx0203e0', 'a1dx0203e1', 'a1dx0203e2', 'a1dx0203e3', 'a1dx0203e4', 'a1dx0203e5', 'a1dx0203e6', 'a1dx0203e7', 'a1dx0203e8', 'a1dx0203e9', 'a1dx0203f0', 'a1dx0203f1', 'a1dx0203f2', 'a1dx0203f3', 'a1dx0203f4', 'a1dx0203f5', 'a1dx0203f6', 'a1dx0203f7', 'a1dx0203f8', 'a1dx0203f9', 'a1dx0203g0', 'a1dx0203g1', 'a1dx0203g2', 'a1dx0203g3', 'a1dx0203g4', 'a1dx0203g5', 'a1dx0203g6', 'a1dx0203g7', 'a1dx0203g8', 'a1dx0203g9', 'a1dx0203h0', 'a1dx0203h1', 'a1dx0203h2', 'a1dx0203h3', 'a1dx0203h4', 'a1dx0203h5', 'a1dx0203h6', 'a1dx0203h7', 'a1dx0203h8', 'a1dx0203h9', 'a1dx0203i0', 'a1dx0203i1', 'a1dx0203i2', 'a1dx0203i3', 'a1dx0203i4', 'a1dx0203i5', 'a1dx0203i6', 'a1dx0203i7', 'a1dx0203i8', 'a1dx0203i9', 'a1dx0203j0', 'a1dx0203j1', 'a1dx0203j2', 'a1dx0203j3', 'a1dx0203j4', 'a1dx0203j5', 'a1dx0203j6', 'a1dx0203j7', 'a1dx0203j8', 'a1dx0203j9', 'a1dx0203k0', 'a1dx0203k1', 'a1dx0203k2', 'a1dx0203k3', 'a1dx0203k4', 'a1dx0203k5', 'a1dx0203k6', 'a1dx0203k7', 'a1dx0203k8', 'a1dx0203k9', 'a1dx0203l0', 'a1dx0203l1', 'a1dx0203l2', 'a1dx0203l3', 'a1dx0203l4', 'a1dx0203l5', 'a1dx0203l6', 'a1dx0203l7', 'a1dx0203l8', 'a1dx0203l9', 'a1dx0203m0', 'a1dx0203m1', 'a1dx0203m2', 'a1dx0203m3', 'a1dx0203m4', 'a1dx0203m5', 'a1dx0203m6', 'a1dx0203m7', 'a1dx0203m8', 'a1dx0203m9', 'a1dx0203n0', 'a1dx0203n1', 'a1dx0203n2', 'a1dx0203n3', 'a1dx0203n4', 'a1dx0203n5', 'a1dx0203n6', 'a1dx0203n7', 'a1dx0203n8', 'a1dx0203n9', 'a1dx0203o0', 'a1dx0203o1', 'a1dx0203o2', 'a1dx0203o3', 'a1dx0203o4', 'a1dx0203o5', 'a1dx0203o6', 'a1dx0203o7', 'a1dx0203o8', 'a1dx0203o9', 'a1dx0203p0', 'a1dx0203p1', 'a1dx0203p2', 'a1dx0203p3', 'a1dx0203p4', 'a1dx0203p5', 'a1dx0203p6', 'a1dx0203p7', 'a1dx0203p8', 'a1dx0203p9', 'a1dx0203q0', 'a1dx0203q1', 'a1dx0203q2', 'a1dx0203q3', 'a1dx0203q4', 'a1dx0203q5', 'a1dx0203q6', 'a1dx0203q7', 'a1dx0203q8', 'a1dx0203q9', 'a1dx0203r0', 'a1dx0203r1', 'a1dx0203r2', 'a1dx0203r3', 'a1dx0203r4', 'a1dx0203r5', 'a1dx0203r6', 'a1dx0203r7', 'a1dx0203r8', 'a1dx0203r9', 'a1dx0203s0', 'a1dx0203s1', 'a1dx0203s2', 'a1dx0203s3', 'a1dx0203s4', 'a1dx0203s5', 'a1dx0203s6', 'a1dx0203s7', 'a1dx0203s8', 'a1dx0203s9', 'a1dx0203t0', 'a1dx0203t1', 'a1dx0203t2', 'a1dx0203t3', 'a1dx0203t4', 'a1dx0203t5', 'a1dx0203t6', 'a1dx0203t7', 'a1dx0203t8', 'a1dx0203t9', 'a1dx0203u0', 'a1dx0203u1', 'a1dx0203u2', 'a1dx0203u3', 'a1dx0203u4', 'a1dx0203u5', 'a1dx0203u6', 'a1dx0203u7', 'a1dx0203u8', 'a1dx0203u9', 'a1dx0203v0', 'a1dx0203v1', 'a1dx0203v2', 'a1dx0203v3', 'a1dx0203v4', 'a1dx0203v5', 'a1dx0203v6', 'a1dx0203v7', 'a1dx0203v8', 'a1dx0203v9', 'a1dx0203w0', 'a1dx0203w1', 'a1dx0203w2', 'a1dx0203w3', 'a1dx0203w4', 'a1dx0203w5', 'a1dx0203w6', 'a1dx0203w7', 'a1dx0203w8', 'a1dx0203w9', 'a1dx0203x0', 'a1dx0203x1', 'a1dx0203x2', 'a1dx0203x3', 'a1dx0203x4', 'a1dx0203x5', 'a1dx0203x6', 'a1dx0203x7', 'a1dx0203x8', 'a1dx0203x9', 'a1dx0203y0', 'a1dx0203y1', 'a1dx0203y2', 'a1dx0203y3', 'a1dx0203y4', 'a1dx0203y5', 'a1dx0203y6', 'a1dx0203y7', 'a1dx0203y8', 'a1dx0203y9', 'a1dx0203z0', 'a1dx0203z1', 'a1dx0203z2', 'a1dx0203z3', 'a1dx0203z4', 'a1dx0203z5', 'a1dx0203z6', 'a1dx0203z7', 'a1dx0203z8', 'a1dx0203z9', 'a1dx0203aa', 'a1dx0203ab', 'a1dx0203ac', 'a1dx0203ad', 'a1dx0203ae', 'a1dx0203af', 'a1dx0203ag', 'a1dx0203ah', 'a1dx0203ai', 'a1dx0203aj', 'a1dx0203ak', 'a1dx0203al', 'a1dx0203am', 'a1dx0203an', 'a1dx0203ao', 'a1dx0203ap', 'a1dx0203aq', 'a1dx0203ar', 'a1dx0203as', 'a1dx0203at', 'a1dx0203au', 'a1dx0203av', 'a1dx0203aw', 'a1dx0203ax', 'a1dx0203ay', 'a1dx0203az', 'a1dx0203ba', 'a1dx0203bb', 'a1dx0203bc', 'a1dx0203bd', 'a1dx0203be', 'a1dx0203bf', 'a1dx0203bg', 'a1dx0203bh', 'a1dx0203bi', 'a1dx0203bj', 'a1dx0203bk', 'a1dx0203bl', 'a1dx0203bm', 'a1dx0203bn', 'a1dx0203bo', 'a1dx0203bp', 'a1dx0203bq', 'a1dx0203br', 'a1dx0203bs', 'a1dx0203bt', 'a1dx0203bu', 'a1dx0203bv', 'a1dx0203bw', 'a1dx0203bx', 'a1dx0203by', 'a1dx0203bz', 'a1dx0203ca', 'a1dx0203cb', 'a1dx0203cc', 'a1dx0203cd', 'a1dx0203ce', 'a1dx0203cf', 'a1dx0203cg', 'a1dx0203ch', 'a1dx0203ci', 'a1dx0203cj', 'a1dx0203ck', 'a1dx0203cl', 'a1dx0203cm', 'a1dx0203cn', 'a1dx0203co', 'a1dx0203cp', 'a1dx0203cq', 'a1dx0203cr', 'a1dx0203cs', 'a1dx0203ct', 'a1dx0203cu', 'a1dx0203cv', 'a1dx0203cw', 'a1dx0203cx', 'a1dx0203cy', 'a1dx0203cz', 'a1dx0203da', 'a1dx0203db', 'a1dx0203dc', 'a1dx0203dd', 'a1dx0203de', 'a1dx0203df', 'a1dx0203dg', 'a1dx0203dh', 'a1dx0203di', 'a1dx0203dj', 'a1dx0203dk', 'a1dx0203dl', 'a1dx0203dm', 'a1dx0203dn', 'a1dx0203do', 'a1dx0203dp', 'a1dx0203dq', 'a1dx0203dr', 'a1dx0203ds', 'a1dx0203dt', 'a1dx0203du', 'a1dx0203dv', 'a1dx0203dw', 'a1dx0203dx', 'a1dx0203dy', 'a1dx0203dz', 'a1dx0203ea', 'a1dx0203eb', 'a1dx0203ec', 'a1dx0203ed', 'a1dx0203ee', 'a1dx0203ef', 'a1dx0203eg', 'a1dx0203eh', 'a1dx0203ei', 'a1dx0203ej', 'a1dx0203ek', 'a1dx0203el', 'a1dx0203em', 'a1dx0203en', 'a1dx0203eo', 'a1dx0203ep', 'a1dx0203eq', 'a1dx0203er', 'a1dx0203es', 'a1dx0203et', 'a1dx0203eu', 'a1dx0203ev', 'a1dx0203ew', 'a1dx0203ex', 'a1dx0203ey', 'a1dx0203ez', 'a1dx0203fa', 'a1dx0203fb', 'a1dx0203fc', 'a1dx0203fd', 'a1dx0203fe', 'a1dx0203ff', 'a1dx0203fg', 'a1dx0203fh', 'a1dx0203fi', 'a1dx0203fj', 'a1dx0203fk', 'a1dx0203fl', 'a1dx0203fm', 'a1dx0203fn', 'a1dx0203fo', 'a1dx0203fp', 'a1dx0203fq', 'a1dx0203fr', 'a1dx0203fs', 'a1dx0203ft', 'a1dx0203fu', 'a1dx0203fv', 'a1dx0203fw', 'a1dx0203fx', 'a1dx0203fy', 'a1dx0203fz', 'a1dx0203ga', 'a1dx0203gb', 'a1dx0203gc', 'a1dx0203gd', 'a1dx0203ge', 'a1dx0203gf', 'a1dx0203gg', 'a1dx0203gh', 'a1dx0203gi', 'a1dx0203gj', 'a1dx0203gk', 'a1dx0203gl', 'a1dx0203gm', 'a1dx0203gn', 'a1dx0203go', 'a1dx0203gp', 'a1dx0203gq', 'a1dx0203gr', 'a1dx0203gs', 'a1dx0203gt', 'a1dx0203gu', 'a1dx0203gv', 'a1dx0203gw', 'a1dx0203gx', 'a1dx0203gy', 'a1dx0203gz', 'a1dx0203ha', 'a1dx0203hb', 'a1dx0203hc', 'a1dx0203hd', 'a1dx0203he', 'a1dx0203hf', 'a1dx0203hg', 'a1dx0203hh', 'a1dx0203hi', 'a1dx0203hj', 'a1dx0203hk', 'a1dx0203hl', 'a1dx0203hm', 'a1dx0203hn', 'a1dx0203ho', 'a1dx0203hp', 'a1dx0203hq', 'a1dx0203hr', 'a1dx0203hs', 'a1dx0203ht', 'a1dx0203hu', 'a1dx0203hv', 'a1dx0203hw', 'a1dx0203hx', 'a1dx0203hy', 'a1dx0203hz', 'a1dx0203ia', 'a1dx0203ib', 'a1dx0203ic', 'a1dx0203id', 'a1dx0203ie', 'a1dx0203if', 'a1dx0203ig', 'a1dx0203ih', 'a1dx0203ii', 'a1dx0203ij', 'a1dx0203ik', 'a1dx0203il', 'a1dx0203im', 'a1dx0203in', 'a1dx0203io', 'a1dx0203ip', 'a1dx0203iq', 'a1dx0203ir', 'a1dx0203is', 'a1dx0203it', 'a1dx0203iu', 'a1dx0203iv', 'a1dx0203iw', 'a1dx0203ix', 'a1dx0203iy', 'a1dx0203iz', 'a1dx0203ja', 'a1dx0203jb', 'a1dx0203jc', 'a1dx0203jd', 'a1dx0203je', 'a1dx0203jf', 'a1dx0203jg', 'a1dx0203jh', 'a1dx0203ji', 'a1dx0203jj', 'a1dx0203jk', 'a1dx0203jl', 'a1dx0203jm', 'a1dx0203jn', 'a1dx0203jo', 'a1dx0203jp', 'a1dx0203jq', 'a1dx0203jr', 'a1dx0203js', 'a1dx0203jt', 'a1dx0203ju', 'a1dx0203jv', 'a1dx0203jw', 'a1dx0203jx', 'a1dx0203jy', 'a1dx0203jz', 'a1dx0203ka', 'a1dx0203kb', 'a1dx0203kc', 'a1dx0203kd', 'a1dx0203ke', 'a1dx0203kf', 'a1dx0203kg', 'a1dx0203kh', 'a1dx0203ki', 'a1dx0203kj', 'a1dx0203kk', 'a1dx0203kl', 'a1dx0203km', 'a1dx0203kn', 'a1dx0203ko', 'a1dx0203kp', 'a1dx0203kq', 'a1dx0203kr', 'a1dx0203ks', 'a1dx0203kt', 'a1dx0203ku', 'a1dx0203kv', 'a1dx0203kw', 'a1dx0203kx', 'a1dx0203ky', 'a1dx0203kz', 'a1dx0203la', 'a1dx0203lb', 'a1dx0203lc', 'a1dx0203ld', 'a1dx0203le', 'a1dx0203lf', 'a1dx0203lg', 'a1dx0203lh', 'a1dx0203li', 'a1dx0203lj', 'a1dx0203lk', 'a1dx0203ll', 'a1dx0203lm', 'a1dx0203ln', 'a1dx0203lo', 'a1dx0203lp', 'a1dx0203lq', 'a1dx0203lr', 'a1dx0203ls', 'a1dx0203lt', 'a1dx0203lu', 'a1dx0203lv', 'a1dx0203lw', 'a1dx0203lx', 'a1dx0203ly', 'a1dx0203lz', 'a1dx0203ma', 'a1dx0203mb', 'a1dx0203mc', 'a1dx0203md', 'a1dx0203me', 'a1dx0203mf', 'a1dx0203mg', 'a1dx0203mh', 'a1dx0203mi', 'a1dx0203mj', 'a1dx0203mk', 'a1dx0203ml', 'a1dx0203mm', 'a1dx0203mn', 'a1dx0203mo', 'a1dx0203mp', 'a1dx0203mq', 'a1dx0203mr', 'a1dx0203ms', 'a1dx0203mt', 'a1dx0203mu', 'a1dx0203mv', 'a1dx0203mw', 'a1dx0203mx', 'a1dx0203my', 'a1dx0203mz', 'a1dx0203na', 'a1dx0203nb', 'a1dx0203nc', 'a1dx0203nd', 'a1dx0203ne', 'a1dx0203nf', 'a1dx0203ng', 'a1dx0203nh', 'a1dx0203ni', 'a1dx0203nj', 'a1dx0203nk', 'a1dx0203nl', 'a1dx0203nm', 'a1dx0203nn', 'a1dx0203no', 'a1dx0203np', 'a1dx0203nq', 'a1dx0203nr', 'a1dx0203ns', 'a1dx0203nt', 'a1dx0203nu', 'a1dx0203nv', 'a1dx0203nw', 'a1dx0203nx', 'a1dx0203ny', 'a1dx0203nz', 'a1dx0203oa', 'a1dx0203ob', 'a1dx0203oc', 'a1dx0203od', 'a1dx0203oe', 'a1dx0203of', 'a1dx0203og', 'a1dx0203oh', 'a1dx0203oi', 'a1dx0203oj', 'a1dx0203ok', 'a1dx0203ol', 'a1dx0203om', 'a1dx0203on', 'a1dx0203oo', 'a1dx0203op', 'a1dx0203oq', 'a1dx0203or', 'a1dx0203os', 'a1dx0203ot', 'a1dx0203ou', 'a1dx0203ov', 'a1dx0203ow', 'a1dx0203ox', 'a1dx0203oy', 'a1dx0203oz', 'a1dx0203pa', 'a1dx0203pb', 'a1dx0203pc', 'a1dx0203pd', 'a1dx0203pe', 'a1dx0203pf', 'a1dx0203pg', 'a1dx0203ph', 'a1dx0203pi', 'a1dx0203pj', 'a1dx0203pk', 'a1dx0203pl', 'a1dx0203pm', 'a1dx0203pn', 'a1dx0203po', 'a1dx0203pp', 'a1dx0203pq', 'a1dx0203pr', 'a1dx0203ps', 'a1dx0203pt', 'a1dx0203pu', 'a1dx0203pv', 'a1dx0203pw', 'a1dx0203px', 'a1dx0203py', 'a1dx0203pz', 'a1dx0203qa', 'a1dx0203qb', 'a1dx0203qc', 'a1dx0203qd', 'a1dx0203qe', 'a1dx0203qf', 'a1dx0203qg', 'a1dx0203qh', 'a1dx0203qi', 'a1dx0203qj', 'a1dx0203qk', 'a1dx0203ql', 'a1dx0203qm', 'a1dx0203qn', 'a1dx0203qo', 'a1dx0203qp', 'a1dx0203qq', 'a1dx0203qr', 'a1dx0203qs', 'a1dx0203qt', 'a1dx0203qu', 'a1dx0203qv', 'a1dx0203qw', 'a1dx0203qx', 'a1dx0203qy', 'a1dx0203qz', 'a1dx0203ra', 'a1dx0203rb', 'a1dx0203rc', 'a1dx0203rd', 'a1dx0203re', 'a1dx0203rf', 'a1dx0203rg', 'a1dx0203rh']

toten_list=[]
name_list=["A","B","C","D"]
#请求登录接口，获取toten
def get_toten(i):
    global toten,name
    name=num[i]
    # name=num
    # name = "fceshi0" + str(int(i))
    url="http://192.168.10.120:6210/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data ={
    "userName":name,
    "password":"991444c1f732105f81fa51df09c2619d",
    "loginUrl":"http://192.168.10.120:96"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    #print(results)
    toten=results['data']['data']['accessCode']
    toten_list.append(toten)
    if results['code'] == 0:
        print("登录用户："+name)
        print("toten:" + toten)
    else:
        print(results['code'], results['message'])
    # print("登录用户：" + name)
    # print("toten:" + toten)

    return toten

def get_register01(i):
    global name01
    # name01=str(name[j])+str(int(j))
    name01="fceshi0"+str(int(i)+7)
    url = "http://192.168.10.120:6210/creditUser/setCreditUserLoginAccount?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "loginAccount": name01,
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        print(str(name01) + "修改账号成功")
    else:
        print(results['code'], results['message'])

def get_register02(i):
    password="Bfty123456"
    url = "http://192.168.10.120:6210/creditUser/setCreditUserPassword?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "oldPassword": password,
        "newPassword":password
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        # print(str(name01) + "密码修改成功")
        print(str(name) + "密码修改成功")
        time.sleep(0.5)
    else:
        print(results['code'], results['message'])




threads = []
t1=threading.Thread(target=get_toten,args=())
threads.append(t1)
# t2=threading.Thread(target=get_register01,args=())
# threads.append(t2)
# t3=threading.Thread(target=get_register02,args=())
# threads.append(t3)


# if __name__=='__main__':
#     for j in range(173, len(num)):
#         print(j)
#         get_toten()
#         if j==173:
#             time.sleep(3)
#         else:
#             pass
#         try:
#             _thread.start_new_thread(get_register01, ())
#             _thread.start_new_thread(get_register02, ())
#         except:
#             print
#             "Error: unable to start thread"
#         print("---------------------------------------------------------分割线------------------------------------------------------------------")


# if __name__=='__main__':
#     for i in range(0, len(num)):
#         print(i)
#         get_toten(i)
#         get_register01(i)
#         # get_register02(i)

if __name__=='__main__':
    for i in range(0, 965):
        print(i)
        get_toten(i)
        get_register01(i)
        get_register02(i)





# if __name__=='__main__':
#     for j in range(1, 401):
#         print(j)
#         for t in threads:
#             t.setDaemon(True)
#             t.start()
#         for t in threads:
#             t.join()

# if __name__=='__main__':
#     with ThreadPoolExecutor(max_workers=10) as t:  # 创建一个最大容纳数量为5的线程池
#         for i in range(0, len(num)):
#             task1 = t.submit(get_toten,i)
#         time.sleep(100)
#         for j in range(0,len(toten_list)):
#             task2=t.submit(get_register01,j)
#             task2=t.submit(get_register02,j)





