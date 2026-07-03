#!/usr/bin/env node
/**
 * Copy the local WASM modules (PyMuPDF, Ghostscript, cpdf, OCR) into dist/wasm
 * so the desktop (Tauri) build works fully offline.
 *
 * The web/LAN build does NOT run this — those deployments either serve the
 * modules from a CDN or bake `wasm/` in via Docker. This script only runs as
 * part of `npm run build:tauri`, keeping the web build output unchanged.
 *
 * Cross-platform (used by the macOS/Windows/Linux CI matrix) — pure Node, no
 * shell `cp -r`.
 */
import { cp, mkdir, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');
const src = resolve(root, 'wasm');
const destRoot = resolve(root, 'dist');
const dest = resolve(destRoot, 'wasm');

async function assertDir(p, label) {
  try {
    const s = await stat(p);
    if (!s.isDirectory()) throw new Error(`${label} is not a directory: ${p}`);
  } catch {
    throw new Error(
      `${label} not found: ${p}\n` +
        (label === 'dist/'
          ? 'Run the frontend build first (vite build).'
          : 'The offline WASM modules are missing from the repo.')
    );
  }
}

async function main() {
  await assertDir(src, 'wasm/ source');
  await assertDir(destRoot, 'dist/');
  await mkdir(dest, { recursive: true });
  await cp(src, dest, { recursive: true });
  console.log(`[copy-wasm] Copied ${src} -> ${dest}`);
}

main().catch((err) => {
  console.error(`[copy-wasm] ${err.message}`);
  process.exit(1);
});
