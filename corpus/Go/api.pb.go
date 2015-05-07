package proto

import proto1 "github.com/gogo/protobuf/proto"
import math "math"

var _ = proto1.Marshal
var _ = math.Inf

type ClientCmdID struct {
	WallTime         int64  `protobuf:"varint,1,opt,name=wall_time" json:"wall_time"`
	Random           int64  `protobuf:"varint,2,opt,name=random" json:"random"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ClientCmdID) Reset()         { *m = ClientCmdID{} }
func (m *ClientCmdID) String() string { return proto1.CompactTextString(m) }
func (*ClientCmdID) ProtoMessage()    {}

func (m *ClientCmdID) GetWallTime() int64 {
	if m != nil {
		return m.WallTime
	}
	return 0
}

func (m *ClientCmdID) GetRandom() int64 {
	if m != nil {
		return m.Random
	}
	return 0
}

type RequestHeader struct {
	Timestamp        Timestamp    `protobuf:"bytes,1,opt,name=timestamp" json:"timestamp"`
	CmdID            ClientCmdID  `protobuf:"bytes,2,opt,name=cmd_id" json:"cmd_id"`
	Key              Key          `protobuf:"bytes,3,opt,name=key,customtype=Key" json:"key"`
	EndKey           Key          `protobuf:"bytes,4,opt,name=end_key,customtype=Key" json:"end_key"`
	User             string       `protobuf:"bytes,5,opt,name=user" json:"user"`
	Replica          Replica      `protobuf:"bytes,6,opt,name=replica" json:"replica"`
	RaftID           int64        `protobuf:"varint,7,opt,name=raft_id" json:"raft_id"`
	UserPriority     *int32       `protobuf:"varint,8,opt,name=user_priority,def=1" json:"user_priority,omitempty"`
	Txn              *Transaction `protobuf:"bytes,9,opt,name=txn" json:"txn,omitempty"`
	XXX_unrecognized []byte       `json:"-"`
}

func (m *RequestHeader) Reset()         { *m = RequestHeader{} }
func (m *RequestHeader) String() string { return proto1.CompactTextString(m) }
func (*RequestHeader) ProtoMessage()    {}

const Default_RequestHeader_UserPriority int32 = 1

func (m *RequestHeader) GetTimestamp() Timestamp {
	if m != nil {
		return m.Timestamp
	}
	return Timestamp{}
}

func (m *RequestHeader) GetCmdID() ClientCmdID {
	if m != nil {
		return m.CmdID
	}
	return ClientCmdID{}
}

func (m *RequestHeader) GetUser() string {
	if m != nil {
		return m.User
	}
	return ""
}

func (m *RequestHeader) GetReplica() Replica {
	if m != nil {
		return m.Replica
	}
	return Replica{}
}

func (m *RequestHeader) GetRaftID() int64 {
	if m != nil {
		return m.RaftID
	}
	return 0
}

func (m *RequestHeader) GetUserPriority() int32 {
	if m != nil && m.UserPriority != nil {
		return *m.UserPriority
	}
	return Default_RequestHeader_UserPriority
}

func (m *RequestHeader) GetTxn() *Transaction {
	if m != nil {
		return m.Txn
	}
	return nil
}

type ResponseHeader struct {
	Error            *Error       `protobuf:"bytes,1,opt,name=error" json:"error,omitempty"`
	Timestamp        Timestamp    `protobuf:"bytes,2,opt,name=timestamp" json:"timestamp"`
	Txn              *Transaction `protobuf:"bytes,3,opt,name=txn" json:"txn,omitempty"`
	XXX_unrecognized []byte       `json:"-"`
}

func (m *ResponseHeader) Reset()         { *m = ResponseHeader{} }
func (m *ResponseHeader) String() string { return proto1.CompactTextString(m) }
func (*ResponseHeader) ProtoMessage()    {}

func (m *ResponseHeader) GetError() *Error {
	if m != nil {
		return m.Error
	}
	return nil
}

func (m *ResponseHeader) GetTimestamp() Timestamp {
	if m != nil {
		return m.Timestamp
	}
	return Timestamp{}
}

func (m *ResponseHeader) GetTxn() *Transaction {
	if m != nil {
		return m.Txn
	}
	return nil
}

type ContainsRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ContainsRequest) Reset()         { *m = ContainsRequest{} }
func (m *ContainsRequest) String() string { return proto1.CompactTextString(m) }
func (*ContainsRequest) ProtoMessage()    {}

type ContainsResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Exists           bool   `protobuf:"varint,2,opt,name=exists" json:"exists"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ContainsResponse) Reset()         { *m = ContainsResponse{} }
func (m *ContainsResponse) String() string { return proto1.CompactTextString(m) }
func (*ContainsResponse) ProtoMessage()    {}

func (m *ContainsResponse) GetExists() bool {
	if m != nil {
		return m.Exists
	}
	return false
}

type GetRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *GetRequest) Reset()         { *m = GetRequest{} }
func (m *GetRequest) String() string { return proto1.CompactTextString(m) }
func (*GetRequest) ProtoMessage()    {}

type GetResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Value            *Value `protobuf:"bytes,2,opt,name=value" json:"value,omitempty"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *GetResponse) Reset()         { *m = GetResponse{} }
func (m *GetResponse) String() string { return proto1.CompactTextString(m) }
func (*GetResponse) ProtoMessage()    {}

func (m *GetResponse) GetValue() *Value {
	if m != nil {
		return m.Value
	}
	return nil
}

type PutRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Value            Value  `protobuf:"bytes,2,opt,name=value" json:"value"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *PutRequest) Reset()         { *m = PutRequest{} }
func (m *PutRequest) String() string { return proto1.CompactTextString(m) }
func (*PutRequest) ProtoMessage()    {}

func (m *PutRequest) GetValue() Value {
	if m != nil {
		return m.Value
	}
	return Value{}
}

type PutResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *PutResponse) Reset()         { *m = PutResponse{} }
func (m *PutResponse) String() string { return proto1.CompactTextString(m) }
func (*PutResponse) ProtoMessage()    {}

type ConditionalPutRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Value            Value  `protobuf:"bytes,2,opt,name=value" json:"value"`
	ExpValue         *Value `protobuf:"bytes,3,opt,name=exp_value" json:"exp_value,omitempty"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ConditionalPutRequest) Reset()         { *m = ConditionalPutRequest{} }
func (m *ConditionalPutRequest) String() string { return proto1.CompactTextString(m) }
func (*ConditionalPutRequest) ProtoMessage()    {}

func (m *ConditionalPutRequest) GetValue() Value {
	if m != nil {
		return m.Value
	}
	return Value{}
}

func (m *ConditionalPutRequest) GetExpValue() *Value {
	if m != nil {
		return m.ExpValue
	}
	return nil
}

type ConditionalPutResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ConditionalPutResponse) Reset()         { *m = ConditionalPutResponse{} }
func (m *ConditionalPutResponse) String() string { return proto1.CompactTextString(m) }
func (*ConditionalPutResponse) ProtoMessage()    {}

type IncrementRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Increment        int64  `protobuf:"varint,2,opt,name=increment" json:"increment"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *IncrementRequest) Reset()         { *m = IncrementRequest{} }
func (m *IncrementRequest) String() string { return proto1.CompactTextString(m) }
func (*IncrementRequest) ProtoMessage()    {}

func (m *IncrementRequest) GetIncrement() int64 {
	if m != nil {
		return m.Increment
	}
	return 0
}

type IncrementResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	NewValue         int64  `protobuf:"varint,2,opt,name=new_value" json:"new_value"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *IncrementResponse) Reset()         { *m = IncrementResponse{} }
func (m *IncrementResponse) String() string { return proto1.CompactTextString(m) }
func (*IncrementResponse) ProtoMessage()    {}

func (m *IncrementResponse) GetNewValue() int64 {
	if m != nil {
		return m.NewValue
	}
	return 0
}

type DeleteRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *DeleteRequest) Reset()         { *m = DeleteRequest{} }
func (m *DeleteRequest) String() string { return proto1.CompactTextString(m) }
func (*DeleteRequest) ProtoMessage()    {}

type DeleteResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *DeleteResponse) Reset()         { *m = DeleteResponse{} }
func (m *DeleteResponse) String() string { return proto1.CompactTextString(m) }
func (*DeleteResponse) ProtoMessage()    {}

type DeleteRangeRequest struct {
	RequestHeader      `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	MaxEntriesToDelete int64  `protobuf:"varint,2,opt,name=max_entries_to_delete" json:"max_entries_to_delete"`
	XXX_unrecognized   []byte `json:"-"`
}

func (m *DeleteRangeRequest) Reset()         { *m = DeleteRangeRequest{} }
func (m *DeleteRangeRequest) String() string { return proto1.CompactTextString(m) }
func (*DeleteRangeRequest) ProtoMessage()    {}

func (m *DeleteRangeRequest) GetMaxEntriesToDelete() int64 {
	if m != nil {
		return m.MaxEntriesToDelete
	}
	return 0
}

type DeleteRangeResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	NumDeleted       int64  `protobuf:"varint,2,opt,name=num_deleted" json:"num_deleted"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *DeleteRangeResponse) Reset()         { *m = DeleteRangeResponse{} }
func (m *DeleteRangeResponse) String() string { return proto1.CompactTextString(m) }
func (*DeleteRangeResponse) ProtoMessage()    {}

func (m *DeleteRangeResponse) GetNumDeleted() int64 {
	if m != nil {
		return m.NumDeleted
	}
	return 0
}

type ScanRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	MaxResults       int64  `protobuf:"varint,2,opt,name=max_results" json:"max_results"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ScanRequest) Reset()         { *m = ScanRequest{} }
func (m *ScanRequest) String() string { return proto1.CompactTextString(m) }
func (*ScanRequest) ProtoMessage()    {}

func (m *ScanRequest) GetMaxResults() int64 {
	if m != nil {
		return m.MaxResults
	}
	return 0
}

type ScanResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Rows             []KeyValue `protobuf:"bytes,2,rep,name=rows" json:"rows"`
	XXX_unrecognized []byte     `json:"-"`
}

func (m *ScanResponse) Reset()         { *m = ScanResponse{} }
func (m *ScanResponse) String() string { return proto1.CompactTextString(m) }
func (*ScanResponse) ProtoMessage()    {}

func (m *ScanResponse) GetRows() []KeyValue {
	if m != nil {
		return m.Rows
	}
	return nil
}

type EndTransactionRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Commit           bool          `protobuf:"varint,2,opt,name=commit" json:"commit"`
	SplitTrigger     *SplitTrigger `protobuf:"bytes,3,opt,name=split_trigger" json:"split_trigger,omitempty"`
	MergeTrigger     *MergeTrigger `protobuf:"bytes,4,opt,name=merge_trigger" json:"merge_trigger,omitempty"`
	XXX_unrecognized []byte        `json:"-"`
}

func (m *EndTransactionRequest) Reset()         { *m = EndTransactionRequest{} }
func (m *EndTransactionRequest) String() string { return proto1.CompactTextString(m) }
func (*EndTransactionRequest) ProtoMessage()    {}

func (m *EndTransactionRequest) GetCommit() bool {
	if m != nil {
		return m.Commit
	}
	return false
}

func (m *EndTransactionRequest) GetSplitTrigger() *SplitTrigger {
	if m != nil {
		return m.SplitTrigger
	}
	return nil
}

func (m *EndTransactionRequest) GetMergeTrigger() *MergeTrigger {
	if m != nil {
		return m.MergeTrigger
	}
	return nil
}

type EndTransactionResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	CommitWait       int64  `protobuf:"varint,2,opt,name=commit_wait" json:"commit_wait"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *EndTransactionResponse) Reset()         { *m = EndTransactionResponse{} }
func (m *EndTransactionResponse) String() string { return proto1.CompactTextString(m) }
func (*EndTransactionResponse) ProtoMessage()    {}

func (m *EndTransactionResponse) GetCommitWait() int64 {
	if m != nil {
		return m.CommitWait
	}
	return 0
}

type ReapQueueRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	MaxResults       int64  `protobuf:"varint,2,opt,name=max_results" json:"max_results"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *ReapQueueRequest) Reset()         { *m = ReapQueueRequest{} }
func (m *ReapQueueRequest) String() string { return proto1.CompactTextString(m) }
func (*ReapQueueRequest) ProtoMessage()    {}

func (m *ReapQueueRequest) GetMaxResults() int64 {
	if m != nil {
		return m.MaxResults
	}
	return 0
}

type ReapQueueResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Messages         []Value `protobuf:"bytes,2,rep,name=messages" json:"messages"`
	XXX_unrecognized []byte  `json:"-"`
}

func (m *ReapQueueResponse) Reset()         { *m = ReapQueueResponse{} }
func (m *ReapQueueResponse) String() string { return proto1.CompactTextString(m) }
func (*ReapQueueResponse) ProtoMessage()    {}

func (m *ReapQueueResponse) GetMessages() []Value {
	if m != nil {
		return m.Messages
	}
	return nil
}

type EnqueueUpdateRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *EnqueueUpdateRequest) Reset()         { *m = EnqueueUpdateRequest{} }
func (m *EnqueueUpdateRequest) String() string { return proto1.CompactTextString(m) }
func (*EnqueueUpdateRequest) ProtoMessage()    {}

type EnqueueUpdateResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *EnqueueUpdateResponse) Reset()         { *m = EnqueueUpdateResponse{} }
func (m *EnqueueUpdateResponse) String() string { return proto1.CompactTextString(m) }
func (*EnqueueUpdateResponse) ProtoMessage()    {}

type EnqueueMessageRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Msg              Value  `protobuf:"bytes,2,opt,name=msg" json:"msg"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *EnqueueMessageRequest) Reset()         { *m = EnqueueMessageRequest{} }
func (m *EnqueueMessageRequest) String() string { return proto1.CompactTextString(m) }
func (*EnqueueMessageRequest) ProtoMessage()    {}

func (m *EnqueueMessageRequest) GetMsg() Value {
	if m != nil {
		return m.Msg
	}
	return Value{}
}

type EnqueueMessageResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *EnqueueMessageResponse) Reset()         { *m = EnqueueMessageResponse{} }
func (m *EnqueueMessageResponse) String() string { return proto1.CompactTextString(m) }
func (*EnqueueMessageResponse) ProtoMessage()    {}

type RequestUnion struct {
	Contains         *ContainsRequest       `protobuf:"bytes,1,opt,name=contains" json:"contains,omitempty"`
	Get              *GetRequest            `protobuf:"bytes,2,opt,name=get" json:"get,omitempty"`
	Put              *PutRequest            `protobuf:"bytes,3,opt,name=put" json:"put,omitempty"`
	ConditionalPut   *ConditionalPutRequest `protobuf:"bytes,4,opt,name=conditional_put" json:"conditional_put,omitempty"`
	Increment        *IncrementRequest      `protobuf:"bytes,5,opt,name=increment" json:"increment,omitempty"`
	Delete           *DeleteRequest         `protobuf:"bytes,6,opt,name=delete" json:"delete,omitempty"`
	DeleteRange      *DeleteRangeRequest    `protobuf:"bytes,7,opt,name=delete_range" json:"delete_range,omitempty"`
	Scan             *ScanRequest           `protobuf:"bytes,8,opt,name=scan" json:"scan,omitempty"`
	EndTransaction   *EndTransactionRequest `protobuf:"bytes,9,opt,name=end_transaction" json:"end_transaction,omitempty"`
	ReapQueue        *ReapQueueRequest      `protobuf:"bytes,10,opt,name=reap_queue" json:"reap_queue,omitempty"`
	EnqueueUpdate    *EnqueueUpdateRequest  `protobuf:"bytes,11,opt,name=enqueue_update" json:"enqueue_update,omitempty"`
	EnqueueMessage   *EnqueueMessageRequest `protobuf:"bytes,12,opt,name=enqueue_message" json:"enqueue_message,omitempty"`
	XXX_unrecognized []byte                 `json:"-"`
}

func (m *RequestUnion) Reset()         { *m = RequestUnion{} }
func (m *RequestUnion) String() string { return proto1.CompactTextString(m) }
func (*RequestUnion) ProtoMessage()    {}

func (m *RequestUnion) GetContains() *ContainsRequest {
	if m != nil {
		return m.Contains
	}
	return nil
}

func (m *RequestUnion) GetGet() *GetRequest {
	if m != nil {
		return m.Get
	}
	return nil
}

func (m *RequestUnion) GetPut() *PutRequest {
	if m != nil {
		return m.Put
	}
	return nil
}

func (m *RequestUnion) GetConditionalPut() *ConditionalPutRequest {
	if m != nil {
		return m.ConditionalPut
	}
	return nil
}

func (m *RequestUnion) GetIncrement() *IncrementRequest {
	if m != nil {
		return m.Increment
	}
	return nil
}

func (m *RequestUnion) GetDelete() *DeleteRequest {
	if m != nil {
		return m.Delete
	}
	return nil
}

func (m *RequestUnion) GetDeleteRange() *DeleteRangeRequest {
	if m != nil {
		return m.DeleteRange
	}
	return nil
}

func (m *RequestUnion) GetScan() *ScanRequest {
	if m != nil {
		return m.Scan
	}
	return nil
}

func (m *RequestUnion) GetEndTransaction() *EndTransactionRequest {
	if m != nil {
		return m.EndTransaction
	}
	return nil
}

func (m *RequestUnion) GetReapQueue() *ReapQueueRequest {
	if m != nil {
		return m.ReapQueue
	}
	return nil
}

func (m *RequestUnion) GetEnqueueUpdate() *EnqueueUpdateRequest {
	if m != nil {
		return m.EnqueueUpdate
	}
	return nil
}

func (m *RequestUnion) GetEnqueueMessage() *EnqueueMessageRequest {
	if m != nil {
		return m.EnqueueMessage
	}
	return nil
}

type ResponseUnion struct {
	Contains         *ContainsResponse       `protobuf:"bytes,1,opt,name=contains" json:"contains,omitempty"`
	Get              *GetResponse            `protobuf:"bytes,2,opt,name=get" json:"get,omitempty"`
	Put              *PutResponse            `protobuf:"bytes,3,opt,name=put" json:"put,omitempty"`
	ConditionalPut   *ConditionalPutResponse `protobuf:"bytes,4,opt,name=conditional_put" json:"conditional_put,omitempty"`
	Increment        *IncrementResponse      `protobuf:"bytes,5,opt,name=increment" json:"increment,omitempty"`
	Delete           *DeleteResponse         `protobuf:"bytes,6,opt,name=delete" json:"delete,omitempty"`
	DeleteRange      *DeleteRangeResponse    `protobuf:"bytes,7,opt,name=delete_range" json:"delete_range,omitempty"`
	Scan             *ScanResponse           `protobuf:"bytes,8,opt,name=scan" json:"scan,omitempty"`
	EndTransaction   *EndTransactionResponse `protobuf:"bytes,9,opt,name=end_transaction" json:"end_transaction,omitempty"`
	ReapQueue        *ReapQueueResponse      `protobuf:"bytes,10,opt,name=reap_queue" json:"reap_queue,omitempty"`
	EnqueueUpdate    *EnqueueUpdateResponse  `protobuf:"bytes,11,opt,name=enqueue_update" json:"enqueue_update,omitempty"`
	EnqueueMessage   *EnqueueMessageResponse `protobuf:"bytes,12,opt,name=enqueue_message" json:"enqueue_message,omitempty"`
	XXX_unrecognized []byte                  `json:"-"`
}

func (m *ResponseUnion) Reset()         { *m = ResponseUnion{} }
func (m *ResponseUnion) String() string { return proto1.CompactTextString(m) }
func (*ResponseUnion) ProtoMessage()    {}

func (m *ResponseUnion) GetContains() *ContainsResponse {
	if m != nil {
		return m.Contains
	}
	return nil
}

func (m *ResponseUnion) GetGet() *GetResponse {
	if m != nil {
		return m.Get
	}
	return nil
}

func (m *ResponseUnion) GetPut() *PutResponse {
	if m != nil {
		return m.Put
	}
	return nil
}

func (m *ResponseUnion) GetConditionalPut() *ConditionalPutResponse {
	if m != nil {
		return m.ConditionalPut
	}
	return nil
}

func (m *ResponseUnion) GetIncrement() *IncrementResponse {
	if m != nil {
		return m.Increment
	}
	return nil
}

func (m *ResponseUnion) GetDelete() *DeleteResponse {
	if m != nil {
		return m.Delete
	}
	return nil
}

func (m *ResponseUnion) GetDeleteRange() *DeleteRangeResponse {
	if m != nil {
		return m.DeleteRange
	}
	return nil
}

func (m *ResponseUnion) GetScan() *ScanResponse {
	if m != nil {
		return m.Scan
	}
	return nil
}

func (m *ResponseUnion) GetEndTransaction() *EndTransactionResponse {
	if m != nil {
		return m.EndTransaction
	}
	return nil
}

func (m *ResponseUnion) GetReapQueue() *ReapQueueResponse {
	if m != nil {
		return m.ReapQueue
	}
	return nil
}

func (m *ResponseUnion) GetEnqueueUpdate() *EnqueueUpdateResponse {
	if m != nil {
		return m.EnqueueUpdate
	}
	return nil
}

func (m *ResponseUnion) GetEnqueueMessage() *EnqueueMessageResponse {
	if m != nil {
		return m.EnqueueMessage
	}
	return nil
}

type BatchRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Requests         []RequestUnion `protobuf:"bytes,2,rep,name=requests" json:"requests"`
	XXX_unrecognized []byte         `json:"-"`
}

func (m *BatchRequest) Reset()         { *m = BatchRequest{} }
func (m *BatchRequest) String() string { return proto1.CompactTextString(m) }
func (*BatchRequest) ProtoMessage()    {}

func (m *BatchRequest) GetRequests() []RequestUnion {
	if m != nil {
		return m.Requests
	}
	return nil
}

type BatchResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	Responses        []ResponseUnion `protobuf:"bytes,2,rep,name=responses" json:"responses"`
	XXX_unrecognized []byte          `json:"-"`
}

func (m *BatchResponse) Reset()         { *m = BatchResponse{} }
func (m *BatchResponse) String() string { return proto1.CompactTextString(m) }
func (*BatchResponse) ProtoMessage()    {}

func (m *BatchResponse) GetResponses() []ResponseUnion {
	if m != nil {
		return m.Responses
	}
	return nil
}

type AdminSplitRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	SplitKey         Key    `protobuf:"bytes,2,opt,name=split_key,customtype=Key" json:"split_key"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *AdminSplitRequest) Reset()         { *m = AdminSplitRequest{} }
func (m *AdminSplitRequest) String() string { return proto1.CompactTextString(m) }
func (*AdminSplitRequest) ProtoMessage()    {}

type AdminSplitResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *AdminSplitResponse) Reset()         { *m = AdminSplitResponse{} }
func (m *AdminSplitResponse) String() string { return proto1.CompactTextString(m) }
func (*AdminSplitResponse) ProtoMessage()    {}

type AdminMergeRequest struct {
	RequestHeader    `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	SubsumedRange    RangeDescriptor `protobuf:"bytes,2,opt,name=subsumed_range" json:"subsumed_range"`
	XXX_unrecognized []byte          `json:"-"`
}

func (m *AdminMergeRequest) Reset()         { *m = AdminMergeRequest{} }
func (m *AdminMergeRequest) String() string { return proto1.CompactTextString(m) }
func (*AdminMergeRequest) ProtoMessage()    {}

func (m *AdminMergeRequest) GetSubsumedRange() RangeDescriptor {
	if m != nil {
		return m.SubsumedRange
	}
	return RangeDescriptor{}
}

type AdminMergeResponse struct {
	ResponseHeader   `protobuf:"bytes,1,opt,name=header,embedded=header" json:"header"`
	XXX_unrecognized []byte `json:"-"`
}

func (m *AdminMergeResponse) Reset()         { *m = AdminMergeResponse{} }
func (m *AdminMergeResponse) String() string { return proto1.CompactTextString(m) }
func (*AdminMergeResponse) ProtoMessage()    {}

func init() {
}
func (this *RequestUnion) GetValue() interface{} {
	if this.Contains != nil {
		return this.Contains
	}
	if this.Get != nil {
		return this.Get
	}
	if this.Put != nil {
		return this.Put
	}
	if this.ConditionalPut != nil {
		return this.ConditionalPut
	}
	if this.Increment != nil {
		return this.Increment
	}
	if this.Delete != nil {
		return this.Delete
	}
	if this.DeleteRange != nil {
		return this.DeleteRange
	}
	if this.Scan != nil {
		return this.Scan
	}
	if this.EndTransaction != nil {
		return this.EndTransaction
	}
	if this.ReapQueue != nil {
		return this.ReapQueue
	}
	if this.EnqueueUpdate != nil {
		return this.EnqueueUpdate
	}
	if this.EnqueueMessage != nil {
		return this.EnqueueMessage
	}
	return nil
}

func (this *RequestUnion) SetValue(value interface{}) bool {
	switch vt := value.(type) {
	case *ContainsRequest:
		this.Contains = vt
	case *GetRequest:
		this.Get = vt
	case *PutRequest:
		this.Put = vt
	case *ConditionalPutRequest:
		this.ConditionalPut = vt
	case *IncrementRequest:
		this.Increment = vt
	case *DeleteRequest:
		this.Delete = vt
	case *DeleteRangeRequest:
		this.DeleteRange = vt
	case *ScanRequest:
		this.Scan = vt
	case *EndTransactionRequest:
		this.EndTransaction = vt
	case *ReapQueueRequest:
		this.ReapQueue = vt
	case *EnqueueUpdateRequest:
		this.EnqueueUpdate = vt
	case *EnqueueMessageRequest:
		this.EnqueueMessage = vt
	default:
		return false
	}
	return true
}
func (this *ResponseUnion) GetValue() interface{} {
	if this.Contains != nil {
		return this.Contains
	}
	if this.Get != nil {
		return this.Get
	}
	if this.Put != nil {
		return this.Put
	}
	if this.ConditionalPut != nil {
		return this.ConditionalPut
	}
	if this.Increment != nil {
		return this.Increment
	}
	if this.Delete != nil {
		return this.Delete
	}
	if this.DeleteRange != nil {
		return this.DeleteRange
	}
	if this.Scan != nil {
		return this.Scan
	}
	if this.EndTransaction != nil {
		return this.EndTransaction
	}
	if this.ReapQueue != nil {
		return this.ReapQueue
	}
	if this.EnqueueUpdate != nil {
		return this.EnqueueUpdate
	}
	if this.EnqueueMessage != nil {
		return this.EnqueueMessage
	}
	return nil
}

func (this *ResponseUnion) SetValue(value interface{}) bool {
	switch vt := value.(type) {
	case *ContainsResponse:
		this.Contains = vt
	case *GetResponse:
		this.Get = vt
	case *PutResponse:
		this.Put = vt
	case *ConditionalPutResponse:
		this.ConditionalPut = vt
	case *IncrementResponse:
		this.Increment = vt
	case *DeleteResponse:
		this.Delete = vt
	case *DeleteRangeResponse:
		this.DeleteRange = vt
	case *ScanResponse:
		this.Scan = vt
	case *EndTransactionResponse:
		this.EndTransaction = vt
	case *ReapQueueResponse:
		this.ReapQueue = vt
	case *EnqueueUpdateResponse:
		this.EnqueueUpdate = vt
	case *EnqueueMessageResponse:
		this.EnqueueMessage = vt
	default:
		return false
	}
	return true
}
