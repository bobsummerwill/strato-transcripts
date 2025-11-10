#!/usr/bin/env python3
"""Quick script to check available OpenAI models"""
import os
import sys

try:
    import openai
except ImportError:
    print("Error: openai package not installed")
    sys.exit(1)

api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY not set")
    sys.exit(1)

client = openai.OpenAI(api_key=api_key)

print("Fetching available OpenAI models...")
print("="*60)

try:
    models = client.models.list()
    
    # Filter for GPT-4o models
    gpt4o_models = [m for m in models.data if 'gpt-4o' in m.id.lower() or 'chatgpt' in m.id.lower()]
    
    print("\nGPT-4o and ChatGPT Models:")
    print("-"*60)
    for model in sorted(gpt4o_models, key=lambda x: x.id):
        print(f"  {model.id}")
        if hasattr(model, 'created'):
            from datetime import datetime
            created = datetime.fromtimestamp(model.created)
            print(f"    Created: {created.strftime('%Y-%m-%d')}")
    
    print("\n" + "="*60)
    print(f"Total GPT-4o/ChatGPT models: {len(gpt4o_models)}")
    
except Exception as e:
    print(f"Error fetching models: {e}")
    sys.exit(1)
