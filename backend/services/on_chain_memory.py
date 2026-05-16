import os
import json
from typing import Dict, Any, List
from datetime import datetime
import hashlib

class OnChainAIMemory:
    """
    On-Chain AI Memory
    Stores user's past creations on-chain (or Vector DB + Supabase)
    """
    
    def __init__(self):
        # Initialize storage options
        self.use_supabase = bool(os.getenv("SUPABASE_URL") and os.getenv("SUPABASE_KEY"))
        self.use_solana = bool(os.getenv("SOLANA_RPC_URL"))  # Alternative on-chain storage
        
        # In-memory fallback for development
        self.memory_store = []  # In production, this would be replaced with actual DB/chain calls
        
        if self.use_supabase:
            self._init_supabase()
        elif self.use_solana:
            self._init_solana_storage()
        # Otherwise use in-memory (not persistent)
    
    def _init_supabase(self):
        """Initialize Supabase connection"""
        try:
            # In a real implementation:
            # from supabase import create_client
            # self.supabase = create_client(
            #     os.getenv("SUPABASE_URL"),
            #     os.getenv("SUPABASE_KEY")
            # )
            pass
        except Exception as e:
            print(f"Supabase initialization failed: {e}")
            self.use_supabase = False
    
    def _init_solana_storage(self):
        """Initialize Solana storage for on-chain memory"""
        try:
            # In a real implementation:
            # from solana.rpc.api import Client
            # self.solana_client = Client(os.getenv("SOLANA_RPC_URL"))
            pass
        except Exception as e:
            print(f"Solana storage initialization failed: {e}")
            self.use_solana = False
    
    def _generate_memory_id(self, content: Dict[str, Any]) -> str:
        """Generate a unique ID for memory entry"""
        content_str = json.dumps(content, sort_keys=True)
        return hashlib.sha256(content_str.encode()).hexdigest()[:16]
    
    def store_creation(self, creation_data: Dict[str, Any], 
                      user_id: str = "default_user") -> Dict[str, Any]:
        """
        Store a creation in memory (on-chain or vector DB)
        
        Args:
            creation_data: Data about the creation (image, audio, NFT, etc.)
            user_id: Identifier for the user
            
        Returns:
            Storage result with memory ID
        """
        try:
            # Prepare memory entry
            memory_entry = {
                "id": self._generate_memory_id(creation_data),
                "user_id": user_id,
                "timestamp": datetime.now().isoformat(),
                "creation_type": creation_data.get("type", "unknown"),
                "data": creation_data,
                "metadata": {
                    "stored_via": "supabase" if self.use_supabase else 
                                "solana" if self.use_solana else "memory",
                    "version": "1.0"
                }
            }
            
            # Store based on available backend
            if self.use_supabase:
                # result = self.supabase.table('ai_creations').insert(memory_entry).execute()
                # storage_result = {"id": memory_entry["id"], "status": "stored_supabase"}
                storage_result = {"id": memory_entry["id"], "status": "stored_supabase_simulated"}
            elif self.use_solana:
                # In real implementation, store on Solana using Metaplex or similar
                storage_result = {"id": memory_entry["id"], "status": "stored_solana_simulated"}
            else:
                # Fallback to in-memory storage
                self.memory_store.append(memory_entry)
                storage_result = {"id": memory_entry["id"], "status": "stored_memory"}
            
            return {
                "status": "success",
                "memory_id": memory_entry["id"],
                "storage_method": storage_result["status"],
                "timestamp": memory_entry["timestamp"],
                "stored_data": creation_data
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "user_id": user_id
            }
    
    def retrieve_creations(self, user_id: str = "default_user", 
                          limit: int = 10, 
                          creation_type: str = None) -> Dict[str, Any]:
        """
        Retrieve user's past creations
        
        Args:
            user_id: Identifier for the user
            limit: Maximum number of results to return
            creation_type: Filter by creation type (optional)
            
        Returns:
            List of stored creations
        """
        try:
            if self.use_supabase:
                # query = self.supabase.table('ai_creations')\
                #     .select('*')\
                #     .eq('user_id', user_id)\
                #     .order('timestamp', desc=True)\
                #     .limit(limit)
                # if creation_type:
                #     query = query.eq('creation_type', creation_type)
                # result = query.execute()
                # creations = result.data
                creations = []  # Simulated
            elif self.use_solana:
                # Query Solana storage (simplified)
                creations = []  # Simulated
            else:
                # Filter in-memory store
                creations = [
                    entry for entry in self.memory_store
                    if entry["user_id"] == user_id and
                    (creation_type is None or entry["creation_type"] == creation_type)
                ]
                # Sort by timestamp descending and limit
                creations.sort(key=lambda x: x["timestamp"], reverse=True)
                creations = creations[:limit]
            
            return {
                "status": "success",
                "user_id": user_id,
                "count": len(creations),
                "creations": creations,
                "storage_method": "supabase" if self.use_supabase else "solana" if self.use_solana else "memory"
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "user_id": user_id
            }
    
    def delete_creation(self, memory_id: str, user_id: str = "default_user") -> Dict[str, Any]:
        """
        Delete a specific creation from memory
        
        Args:
            memory_id: ID of the memory entry to delete
            user_id: Identifier for the user (for validation)
            
        Returns:
            Deletion result
        """
        try:
            if self.use_supabase:
                # result = self.supabase.table('ai_creations')\
                #     .delete()\
                #     .eq('id', memory_id)\
                #     .eq('user_id', user_id)\
                #     .execute()
                deletion_result = {"status": "deleted_supabase_simulated"}
            elif self.use_solana:
                # In real implementation, mark as deleted on Solana
                deletion_result = {"status": "deleted_solana_simulated"}
            else:
                # Remove from in-memory store
                initial_count = len(self.memory_store)
                self.memory_store = [
                    entry for entry in self.memory_store
                    if not (entry["id"] == memory_id and entry["user_id"] == user_id)
                ]
                deletion_result = {
                    "status": "deleted_from_memory",
                    "deleted_count": initial_count - len(self.memory_store)
                }
            
            return {
                "status": "success",
                "memory_id": memory_id,
                "deletion_result": deletion_result
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "memory_id": memory_id
            }

# Flask API endpoint functions
def create_on_chain_memory_endpoints(app):
    """Create Flask endpoints for on-chain AI memory"""
    from flask import request, jsonify
    
    memory_service = OnChainAIMemory()
    
    @app.route('/api/memory/store', methods=['POST'])
    def store_creation_endpoint():
        try:
            data = request.json
            user_id = data.get("user_id", "default_user")
            creation_data = data.get("creation_data", {})
            
            if not creation_data:
                return jsonify({"error": "Creation data is required"}), 400
            
            result = memory_service.store_creation(creation_data, user_id)
            
            if result["status"] == "success":
                return jsonify(result), 201
            else:
                return jsonify(result), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/memory/retrieve', methods=['GET'])
    def retrieve_creations_endpoint():
        try:
            user_id = request.args.get('user_id', 'default_user')
            limit = int(request.args.get('limit', 10))
            creation_type = request.args.get('type')
            
            result = memory_service.retrieve_creations(user_id, limit, creation_type)
            
            if result["status"] == "success":
                return jsonify(result)
            else:
                return jsonify(result), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/memory/delete/<memory_id>', methods=['DELETE'])
    def delete_creation_endpoint(memory_id):
        try:
            user_id = request.args.get('user_id', 'default_user')
            
            result = memory_service.delete_creation(memory_id, user_id)
            
            if result["status"] == "success":
                return jsonify(result)
            else:
                return jsonify(result), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app